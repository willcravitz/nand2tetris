import sys

# tables to store binary conversions for comps, dests, and jumps
comp_codes = {
    '0': '0101010',
    '1': '0111111',
    '-1': '0111010',
    'D': '0001100',
    'A': '0110000',
    '!D': '0001101',
    '!A': '0110001',
    '-D': '0001111',
    '-A': '0110011',
    'D+1': '0011111',
    'A+1': '0110111',
    'D-1': '0001110',
    'A-1': '0110010',
    'D+A': '0000010',
    'D-A': '0010011',
    'A-D': '0000111',
    'D&A': '0000000',
    'D|A': '0010101',
    'M': '1110000',
    '!M': '1110001',
    '-M': '1110011',
    'M+1': '1110111',
    'M-1': '1110010',
    'D+M': '1000010',
    'D-M': '1010011',
    'M-D': '1000111',
    'D&M': '1000000',
    'D|M': '1010101'
}

dest_codes = {
    'null': '000',
    'M': '001',
    'D': '010',
    'MD': '011',
    'A': '100',
    'AM': '101',
    'AD': '110',
    'AMD': '111'
}

jump_codes = {
    'null': '000',
    'JGT': '001',
    'JEQ': '010',
    'JGE': '011',
    'JLT': '100',
    'JNE': '101',
    'JLE': '110',
    'JMP': '111'
}

# class to convert file into more a more managable form 
class FileHandler:
    def __init__(self, file):
        self.name = str(file)[:-4] # store the name of the file without the extension
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
                    arr.append(line)
        return arr

    # outputs a new file from an array of lines with given extension
    def output(self, arr, extension):
        filename = self.name + '.' + extension
        with open(filename, 'w') as w:
           w.write('\n'.join(arr)) 

# class to handle symbols/labels
class SymbolTable:
    def __init__(self):
        # init with built in symbols
        self.symbols = {
            'SP': 0,
            'LCL': 1,
            'ARG': 2,
            'THIS': 3,
            'THAT': 4,
            'SCREEN': 16384,
            'KBD': 24576
        }
        # create symbols R0-R15
        for i in range(16):
            self.symbols['R' + str(i)] = i
        self.next = 16 # stores next available address

    # scan lines for labels, stores the label, then deletes the line
    def label_scan(self, lines):
        new_lines = []
        counter = 0
        for line in lines:
            if '(' and ')' in line: # if label is found
                label = line[1:line.find(')')] # only store what was inside the parantheses
                self.symbols[label] = counter
            else:
                new_lines.append(line)
                counter += 1
        return new_lines

    # adds new symbol to the table
    def add_symbol(self, new):
        self.symbols[new] = self.next
        self.next += 1 # increment next available address

# standardize each c instruction to be of the form 'dest=comp;jump'
def fill(line):
    if not '=' in line:
        line = 'null=' + line
    if not ';' in line:
        line += ';null'
    return line

# converts decimal number to a specified bit long binary number
def to_bin(bits, decimal):
    binary = ''
    for i in reversed(range(bits)):
        if 2**i <= decimal:
            decimal -= 2**i
            binary += '1'
        else:
            binary += '0'
    return binary

# translates assembly to binary
def translate(line, table):
    output = ''
    if line[0] == '@': # if a-instruction
        output += '0' # starts with a zero
        if line[1:].isdecimal(): # if number address is used
            address = line[1:]
        else: # if symbol is used
            if line[1:] not in table.symbols: # if it's a new symbol then add it to the table
                table.add_symbol(line[1:])
            address = table.symbols[line[1:]]
        output += to_bin(15, int(address)) # convert to address to binary for the next 15 bits of the output
    else:
        line = fill(line) # standardize each c-instruction
        dest = line[:line.find('=')] 
        comp = line[line.find('=')+1:line.find(';')]
        jump = line[line.find(';')+1:]
        # start binary with 111 and convert each instruction to it's binary using the corresponding dictionary
        output = '111' + comp_codes[comp] + dest_codes[dest] + jump_codes[jump]
    return output


Handler = FileHandler(sys.argv[1]) # create FileHandler object with command line file
Table = SymbolTable() # create new SymbolTable object

lines = Table.label_scan(Handler.lines) # scan for labels
outarr = [translate(line, Table) for line in lines] # create a new array with each translated line

Handler.output(outarr, 'hack') # output the new array as a '.hack' file