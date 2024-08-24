import sys
import os

# class to go through a directory and convert files to better form
class FileHandler:
    def __init__(self, a_dir, file_type):
        self.dir = './' + str(a_dir) # store the name of the file without the extension
        self.dirname = os.path.basename(a_dir)
        self.files_type = file_type
        self.files = self.find_files()

    # converts the file into an array of lines and removes whitespace
    def clean_file(self, file):
        arr = []
        with open(file) as f:
            for line in f.readlines():
                if '//' in line:
                    line = line[:line.find('//')] # remove everything after the comment
                line = line.strip() # remove all whitespace from the outsides of the string
                if line: # only keep this line if something is left
                    arr.append(line.split()) # convert line to an array whose elements are each word/number
        return arr
    
    # goes through the directory and returns a list of files vm files with their paths
    def find_files(self):
        arr = []
        for dirpath, dirs, files in os.walk(self.dir):
	        arr = [os.path.join(dirpath, file) for file in files if file.endswith(self.files_type)]
        return arr

    # returns True if directory contains Sys.vm and False if it doesnt
    def has_sys(self):
        for file in self.files:
            if os.path.basename(file) == "Sys.vm":
                return True
        return False

    # outputs a new file from an array of lines with given extension
    def output_file(self, arr, extension):
        filename = self.dir + '/' + self.dirname + extension
        with open(filename, 'w') as w:
           w.write('\n'.join(arr))

# constant section at end of every push
end_push = '''
@SP
A=M
M=D
@SP
M=M+1'''

# constant section at the end of every pop
end_pop = '''
@R15
M=D
@SP
AM=M-1
D=M
@R15
A=M
M=D'''

# push/pop templates and corresponding operations for each memory access command category
mem_commands = {
    'constant': {
        'constant': '',
        'push': '@{}{}\nD=A' + end_push
    },
    'dynamic': {
        'local': 'LCL',
        'argument': 'ARG',
        'this': 'THIS',
        'that': 'THAT',
        'push': '@{}\nD=M\n@{}\nA=D+A\nD=M' + end_push,
        'pop': '@{}\nD=M\n@{}\nD=D+A' + end_pop
    },
    'static': {
        'static': '',
        'push': '@{}.{}\nD=M' + end_push,
        'pop': '@SP\nAM=M-1\nD=M\n@{}.{}\nM=D'
    },
    'temp': {
        'temp': 'R',
        'push': '@{}{}\nD=M' + end_push,
        'pop': '@SP\nAM=M-1\nD=M\n@{}{}\nM=D'
    },
    'pointer': {
        'pointer': '',
        '0': 'THIS',
        '1': 'THAT',
        'push': '@{}{}\nD=M' + end_push,
        'pop': '@SP\nAM=M-1\nD=M\n@{}{}\nM=D'
    }
}

# templates and operations for all arithmetic and logical commands
alu_commands = {
    'binary': {
        'add': '+',
        'sub': '-',
        'and': '&',
        'or': '|',
        'asm': '@SP\nAM=M-1\nD=M\nA=A-1\nM=M{}D'
    },
    'unitary': {
        'neg': '-',
        'not': '!',
        'asm': '@SP\nA=M-1\nM={}M'
    },
    'boolean': {
        'eq': 'JEQ',
        'lt': 'JLT',
        'gt': 'JGT',
        'new_label': 0, # label used for jumps, must be changed for each boolean command
        'asm': '@SP\nA=M-1\nA=A-1\nD=M\nA=A+1\nD=D-M\n@_{1}\nD;{0}\n@_{2}\nD=0;JMP\n(_{1})\nD=-1\n(_{2})\n@SP\nAM=M-1\nA=A-1\nM=D'
    }
}


current_function = 'Sys.init' # let's track the current function so we can name our labels function$label
return_label_unique_maker = 0 # makes your return-adress label unique. 100% Guarenteed!

# returns category of a command
def find_category(a_dict, command):
    for key, item in a_dict.items():
        if command in item.keys():
            return key

# push the the address that pointer p is pointing too
def push_pointer(p):
    return '@{}\nD=M'.format(p) + end_push + '\n'

# translate label c to asm as (function$c)
def label(c):
    return '({}${})\n'.format(current_function, c)

# go to label address and jump unconditionally
def goto(c):
    return '@{}${}\n0;JMP\n'.format(current_function, c)

# go to label address and jump if top of stack is -1
def if_goto(c):
    return '@SP\nAM=M-1\nD=M\n@{}${}\nD;JNE\n'.format(current_function, c)

def call(f, n):
    global return_label_unique_maker
    asm = '@{}$RETURN{}\nD=A'.format(current_function, return_label_unique_maker) + end_push + '\n' # push return
    # save previous function state on the stack
    for pointer in list(mem_commands['dynamic'].values())[:4]:
        asm += push_pointer(pointer)
    asm += '''@SP
D=M
@{}
D=D-A
@5
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@{}
0;JMP
'''.format(n, f) + label('RETURN{}'.format(return_label_unique_maker))
    return_label_unique_maker+=1 # next time we'll have different labels
    return asm

# while loop that repeats the code input
def repeat(f, k, code):
    return '''@{1}
D=A
@R13
M=D
({0}$REPEATLOOP)
@R13
D=M
@{0}$REPEATEND
D;JEQ
{2}
@R13
M=M-1
@{0}$REPEATLOOP
0;JMP
({0}$REPEATEND)
'''.format(f, k, code)

# translate function definition
def func(f, k):
    current_function = f
    return '({})\n'.format(f) + repeat(f, k, '@0\nD=A' + end_push)

# takes from frame-n and puts it into dest
def frame(n, dest):
    return '@{}\nD=A\n@R14\nA=M-D\nD=M\n@{}\nM=D\n'.format(n, dest)

# translate return statement
def ret():
    asm = '@LCL\nD=M\n@R14\nM=D\n'
    asm += frame('5', 'R13')
    asm += '@ARG\nD=M' + end_pop + '\n@ARG\nD=M\n@SP\nM=D+1\n'
    asm += frame('1', 'THAT') + frame('2', 'THIS') + frame('3', 'ARG') + frame('4', 'LCL')
    asm += '@R13\nA=M\n0;JMP'
    return asm

# bootstrap code
init = '@256\nD=A\n@SP\nM=D\n' + call('Sys.init', 0).strip()

def translate(line, file_name):
    if len(line) == 1: # if command is arithmetic/logical or return
        if line[0] == 'return':
            return ret()
        else:
            command = line[0]
            category = find_category(alu_commands, command)
            if category == 'boolean': # create new labels for the next boolean command
                new_label = alu_commands['boolean']['new_label']
                alu_commands['boolean']['new_label'] += 2
                return alu_commands[category]['asm'].format(alu_commands[category][command], str(new_label), str(new_label+1))
            # insert the command's corresponding operation into its template
            return alu_commands[category]['asm'].format(alu_commands[category][command])
    elif len(line) == 2: # program flow
        if line[0] == 'label':
            return label(line[1])
        elif line[0] == 'goto':
            return goto(line[1])
        else:
            return if_goto(line[1])
    else: # function defining and calling or push/pop
        if line[0] == 'function':
            return func(line[1], line[2])
        elif line[0] == 'call':
            return call(line[1], line[2])
        else:
            p, command, n = line # p = push/pop, command = command, n = number
            category = find_category(mem_commands, command)
            if category == 'pointer': # convert pointer's number to this/that
                n = mem_commands['pointer'][n]
            elif category == 'temp': # temp starts at RAM5 so add 5 to n
                n = str(int(n) + 5)
            elif category == 'static':
                mem_commands['static']['static'] = file_name
            # insert the command's corresponding operation into its template
            return mem_commands[category][p].format(mem_commands[category][command], n)

# new file handler object from directory
Handler = FileHandler(sys.argv[1], '.vm')
outarr = []
if Handler.has_sys(): 
    outarr.append(init) # add initialization to the file if it doesn't do it automatically

# go through each file and translate each line
for file in Handler.files:
    file_name = os.path.basename(os.path.splitext(file)[0])
    for line in Handler.clean_file(file):
        outarr.append(translate(line, file_name).strip())

# output a new asm file from the array of translated lines
Handler.output_file(outarr, '.asm')