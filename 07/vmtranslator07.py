import sys

# class to convert file into more a more managable form 
class FileHandler:
    def __init__(self, file, file_type):
        self.name = str(file)[:-1*(len(file_type)+1)] # store the name of the file without the extension
        self.file = file
        self.lines = self.clean()

    # converts the file into an array of lines and removes whitespace
    def clean(self):
        arr = []
        with open(self.file) as f:
            for line in f.readlines():
                if '//' in line:
                    line = line[:line.find('//')] # remove everything after the comment
                line = line.strip() # remove all whitespace from the outsides of the string
                if line: # only keep this line if something is left
                    arr.append(line.split()) # convert line to an array whose elements are each word/number
        return arr

    # outputs a new file from an array of lines with given extension
    def output(self, arr, extension):
        filename = self.name + '.' + extension
        with open(filename, 'w') as w:
           w.write('\n'.join(arr))

Handler = FileHandler(sys.argv[1], 'vm') # create FileHandler object with command line file

# constant section at end of every push
end_push = '''
@SP
A=M
M=D
@SP
M=M+1'''

end_pop = '''
@R15
M=D
@SP
AM=M-1
D=M
@R15
A=M
M=D'''

# push/pop templates and corresponding operatoins for each memory access command category
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
        'static': Handler.name[Handler.name.rfind('/')+1:], # only use the file name, not the file path
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
        'label': 0, # label used for jumps, must be changed for each boolean command
        'asm': '@SP\nA=M-1\nA=A-1\nD=M\nA=A+1\nD=D-M\n@_{1}\nD;{0}\n@_{2}\nD=0;JMP\n(_{1})\nD=-1\n(_{2})\n@SP\nAM=M-1\nA=A-1\nM=D'
    }
}

# returns category of a command
def find_category(a_dict, command):
    for key, item in a_dict.items():
        if command in item.keys():
            return key


def translate(line):
    if len(line) == 1: # if command is arithmetic/logical
        command = line[0]
        category = find_category(alu_commands, command)
        if category == 'boolean': # create new labels for the next boolean command
            label = alu_commands['boolean']['label']
            alu_commands['boolean']['label'] += 2
            return alu_commands[category]['asm'].format(alu_commands[category][command], str(label), str(label+1))
        # insert the command's corresponding operation into its template
        return alu_commands[category]['asm'].format(alu_commands[category][command])
    else:
        p, command, n = line # p = push/pop, command = command, n = number
        category = find_category(mem_commands, command)
        if category == 'pointer': # convert pointer's number to this/that
            n = mem_commands['pointer'][n]
        elif category == 'temp': # temp starts at RAM5 so add 5 to n
            n = str(int(n) + 5)
        # insert the command's corresponding operation into its template
        return mem_commands[category][p].format(mem_commands[category][command], n)

# output the assembly file from an array of translated vm lines
Handler.output([translate(line) for line in Handler.lines], 'asm')