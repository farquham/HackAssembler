#Assembler program for nand 2 tetris wk6
import sys

# unpacks each instruction into its underlying fields pg63
def parser(currentline):
    # ignores blank lines
    if currentline[0] == "\n":
        return
    # ignores commented out lines
    if currentline[0] == "/" and currentline[1] == "/":
        return
    # removes any trailing whitespaces and comments
    currentline = currentline.split()[0]
    # activates the symbol function
    if commandType(currentline[0]) == ("A" or "L"):
        # !!!
        return
    # activates the c command parsers
    elif (commandType(currentline[0]) == "C"):
        command = [pdest(currentline), pcomp(currentline), pjump(currentline)]
        return command

# determines what type of command it is based on the first character
def commandType(firstd):
    if firstd == "@":
        return "A"
    elif firstd == "(":
        return "L"
    else:
        return "C"

# handles the symbol functions for A and L commands
#def symbol(): !!!

# C command format: dest=comp;jump
# parsers a C command to find the destination code
def pdest(line):
    return line.split("=")[0]

# parsers a C command to find the computation code
def pcomp(line):
    comp = line.split("=")[1]
    comp = comp.split(";")[0]
    return comp

# parsers a C command to find the jump code
def pjump(line):
    try:
        return line.split(";")[1]
    except IndexError:
        return ""

# translates each field into its corresponding binary value
def code(commands):
    code[0] = cdest(commands[0])
    code[1] = ccomp(commands[1])
    code[2] = cjump(commands[2])
    return code

def cdest(dcom):
    # !!!

def ccomp(ccom):
    # !!!

def cjump(jcom):
    # !!!

# manages the symbol table
#def symbol_table():

# handles I/O functions
def main():
    file = open(sys.argv[1], 'r')
    lines = file.readlines()
    for line in lines:
        command = parser(line)
        if command == None:
            continue
        else:
            code(command)

if __name__ == "__main__":
    main()


