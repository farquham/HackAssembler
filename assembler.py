#Assembler program for nand 2 tetris wk6
import sys

# unpacks each instruction into its underlying fields pg63
def parser(currentline):
    if currentline[0] == " ":
        return
    if currentline[0] == "/" and currentline[1] == "/":
        return
    for x in currentline:
        if x != "\n":
            print(x)

# translates each field into its corresponding binary value
#def code():

# manages the symbol table
#def symbol_table():

# handles I/O functions
def main():
    file = open(sys.argv[1], 'r')
    lines = file.readlines()
    for line in lines:
        parser(line)

if __name__ == "__main__":
    main()
