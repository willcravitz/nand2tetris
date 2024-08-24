import sys

# lexical elements
lex_elements = {
    'keyword': ['class', 'constructor', 'function', 'method', 'field', 'static', 'var', 'int', 'char', 'boolean', 'void', 'true', 'false', 'null', 'this', 'let', 'do', 'if', 'else', 'while', 'return'],
    'symbol': ['{', '}', '(', ')', '[', ']', '.', ',', ';', '+', '-', '*', '/', '&', '|', '<', '>', '=', '~'],
}

# turn file into one string with new lines removed
def flatten(file):
    comment = False
    new = ''
    with open(file) as f:
        for line in f.readlines():
            if comment:
                if '*/' in line:
                    comment = False
            else:
                if '/**' in line:
                    if '*/' in line:
                        line = ''
                    else:
                        comment = True
                if '//' in line:
                    line = line[:line.find('//')]
                line = line.strip()
                if line:
                    new += line
    return new

# returns array of tokens
def tokenize(flat_file):
    tokens = ['<tokens>']
    curr = 0
    while curr < len(flat_file):
        # if whitespace
        if flat_file[curr].isspace():
            curr += 1
        # if symbol
        elif flat_file[curr] in lex_elements['symbol']:
            tokens.append('<symbol> {} </symbol>'.format(flat_file[curr]))
            curr += 1
        # if string
        elif flat_file[curr] == '"':
            string = ''
            curr += 1
            while flat_file[curr] != '"':
                string += flat_file[curr]
                curr += 1
            tokens.append('<stringConstant> {} </stringConstant>'.format(string))
            curr += 1
        # if integer
        elif flat_file[curr].isdigit():
            num = ''
            while flat_file[curr].isdigit():
                num += flat_file[curr]
                curr += 1
            tokens.append('<integerConstant> {} </integerConstant>'.format(num))
        # if keyword or identifier
        elif flat_file[curr].isalpha():
            word = ''
            while flat_file[curr].isalpha():
                word += flat_file[curr]
                curr += 1
            type_ = 'keyword' if word in lex_elements['keyword'] else 'identifier'  
            tokens.append('<{0}> {1} </{0}>'.format(type_, word))
    tokens.append('</tokens>')
    return tokens

filename = str(sys.argv[1])[:-5]
outarr = tokenize(flatten(sys.argv[1]))
with open('{}T.xml'.format(filename), 'w') as w:
    w.write('\n'.join(outarr))
