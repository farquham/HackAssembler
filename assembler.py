#Assembler program for nand 2 tetris wk6
import sys

# symbolic code file -> binary code file
# handles I/O functions
def main():
    file = open(sys.argv[1], 'r')
    lines = file.readlines()
    file.close()
    nfilename = ((sys.argv[1]).split(".")[0]) + ".hack"
    newfile = open(nfilename, "w")
    for line in lines:
        command = parser(line)
        if command == None:
            continue
        else:
            if len(command) == 3:
                newfile.write(code(command) + "\n")
            else:
                newfile.write(command + "\n")
    newfile.close()

#binum = bin(int(num)).replace("0b", "")
#code = ("0" + str(binum))
#while len(code) <= 15:
#    code = "0" + code
#return code


# line (string) -> line components (list of strings)
# unpacks each instruction into its underlying fields pg63
#elif (commandType(currentline[0]) == "C"):
#    command = [pdest(currentline), pcomp(currentline), pjump(currentline)]
#return command

class Parser:
    # initializes the parser and takes in the lines
    def __init__(self, lines):
        self.counter = 0
        self.lines = lines
        self.line = "Butterfly"
    # () -> Boolean
    # checks if the current line is not the final line
    def hasMoreCommands(self):
        if  self.line != self.lines[-1]:
            return true
        else:
            return false
    # __ -> __
    # advances the parser to the next line and clears whitespace
    def advance(self):
        self.line = self.lines[self.counter]
        self.line = (self.line).strip()
        self.counter += 1

    # string -> string
    # determines what type of command it is based on the first character
    # also identifys comment and blank lines
    def commandType(self):
        if ((self.line)[0]) == "@":
            return "A"
        elif ((self.line)[0]) == "(":
            return "L"
        elif ((self.line)[0]) == "\n":
            return "B"
        elif ((((self.line)[0]) == "/") and (((self.line)[1]) == "/")):
            return "I"
        else:
            return "C"

    # string -> string
    # strips the symbols and returns the decimal/symbol values
    def symbol(self, CT):
        num = (self.line).strip("@()")[1]
        return num

    # line (string) -> string
    # C command format: dest=comp;jump
    # parsers a C command to find the destination code
    def dest(self):
        destcode = (self.line).split("/")[0]
        destcode = destcode.split("=")[0]
        if len(destcode) > 3:
            return ""
        else:
            return destcode

    # line (string) -> string
    # parsers a C command to find the computation code
    def comp(self):
        comp = (self.line).split("/")[0]
        try:
            comp = comp.split("=")[1]
            comp = comp.split(";")[0]
        except IndexError:
            comp = comp.split(";")[0]
        return comp

    # line (string) -> string
    # parsers a C command to find the jump code
    def jump(self):
        jump = (self.line).split("/")[0]
        try:
            return jump.split(";")[1]
        except IndexError:
            return ""


# (list of string) -> string
# translates each field into its corresponding binary value
def code(commands):
    translated = ("111" + (ccomp(commands[1])) + (cdest(commands[0])) +
                  (cjump(commands[2])))
    return translated
class Code:
    def __init__(self):
        pass

    # string -> binary
    # translates the dest mnemonic to binary
    def dest(dcom):
        destdic = {"":"000", "M":"001", "D":"010", "MD":"011",
               "A":"100", "AM":"101", "AD":"110", "AMD":"111"}
        return destdic[dcom]

    # string -> binary
    # translates the comp mnemonic to binary
    def comp(ccom):
        compdic = {"0":"0101010", "1":"0111111", "-1":"0111010", "D":"0001100",
               "A":"0110000", "!D":"0001101", "!A":"0110001", "-D":"0001111",
               "-A":"0110011", "D+1":"0011111", "A+1":"0110111", "D-1":"0001110",
               "A-1":"0110010", "D+A":"0000010", "D-A":"0010011", "A-D":"0000111",
               "D&A":"0000000", "D|A":"0010101", "M":"1110000", "!M":"1110001",
               "-M":"1110011", "M+1":"1110111", "M-1":"1110010", "D+M":"1000010",
               "D-M":"1010011", "M-D":"1000111", "D&M":"1000000", "D|M":"1010101"}
        return compdic[ccom]

    # string -> binary
    # translates the jump mnemonic to binary
    def jump(jcom):
        jumpdic = {"":"000", "JGT":"001", "JEQ":"010", "JGE":"011",
               "JLT":"100", "JNE":"101", "JLE":"110", "JMP":"111"}
        return jumpdic[jcom]


class SymbolTable:
    def __init__(self):
        pass
    def addEntry():
        pass
    def contains():
        pass
    def getAddress():
        pass


if __name__ == "__main__":
    main()
