#Assembler program for nand 2 tetris wk6
import sys


predef_symbols = {"RO":0, "R1":1, "R2":2, "R3":3, "R4":4, "R5":5,
                  "R6":6, "R7":7, "R8":8, "R9":9, "R10":10, "R11":11,
                  "R12":12, "R13":13, "R14":14, "R15":15, "SCREEN":16384,
                  "KBD":24576, "SP":0, "LCL":1, "ARG":2, "THIS":3, "THAT":4}

# symbolic code file -> binary code file
# handles I/O functions
def main():
    st = SymbolTable()
    for x in predef_symbols:
        st.addEntry(x, predef_symbols[x])

    file = open(sys.argv[1], 'r')
    lines = file.readlines()
    file.close()
    p = Parser(lines)

    c = 0
    for x in lines:
        if p.commandType() == ("B" or "I"):
            if p.hasMoreCommands():
                p.advance()
            continue
        if p.commandType() == ("A" or "C"):
            c += 1
            if p.hasMoreCommands():
                p.advance()
            continue
        else:
            c += 1
            st.addEntry(p.symbol(), c)
            if p.hasMoreCommands():
                p.advance()
            continue

    n = 16
    c = Code()
    bilines = []
    for x in lines:
        biline = ""
        if p.commandType() == ("B" or "I" or "L"):
            if p.hasMoreCommands():
                p.advance()
            continue
        if p.commandType() == "A":
            sym = p.symbol()
            if type(sym) !=  "int":
                if sym in st.symboltable:
                    biline = c.acomp(st.getAddress(sym))
                else:
                    st.addEntry(sym, n)
                    biline = c.acomp(n)
                    n += 1
            else:
                biline = c.acomp(int(sym))
            if p.hasMoreCommands():
                p.advance()
        if p.commandType() == "C":
            # !!!
    bilines.append(biline)


   # nfilename = ((sys.argv[1]).split(".")[0]) + ".hack"
   # newfile = open(nfilename, "w")
   #             newfile.write(code(command) + "\n")
   # newfile.close()


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
    def symbol(self):
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


class Code:
    # initializes the code translator and imports the mnemonics
    def __init__(self):
        self.code = "hello"

    # string -> binary
    # translates the dest mnemonic to binary
    def dest(self, destm):
        destdic = {"":"000", "M":"001", "D":"010", "MD":"011",
               "A":"100", "AM":"101", "AD":"110", "AMD":"111"}
        return destdic[destm]

    # string -> binary
    # translates the comp mnemonic to binary
    def comp(self, compm):
        compdic = {"0":"0101010", "1":"0111111", "-1":"0111010", "D":"0001100",
               "A":"0110000", "!D":"0001101", "!A":"0110001", "-D":"0001111",
               "-A":"0110011", "D+1":"0011111", "A+1":"0110111", "D-1":"0001110",
               "A-1":"0110010", "D+A":"0000010", "D-A":"0010011", "A-D":"0000111",
               "D&A":"0000000", "D|A":"0010101", "M":"1110000", "!M":"1110001",
               "-M":"1110011", "M+1":"1110111", "M-1":"1110010", "D+M":"1000010",
               "D-M":"1010011", "M-D":"1000111", "D&M":"1000000", "D|M":"1010101"}
        return compdic[compm]

    # string -> binary
    # translates the jump mnemonic to binary
    def jump(self, jumpm):
        jumpdic = {"":"000", "JGT":"001", "JEQ":"010", "JGE":"011",
               "JLT":"100", "JNE":"101", "JLE":"110", "JMP":"111"}
        return jumpdic[self.jumpm]

    # string -> binary
    # translates A commands to binary
    def acomp(self, num):
        binum = bin(int(num)).replace("0b", "")
        code = ("0" + str(binum))
        while len(code) <= 15:
            code = "0" + code
        return code


class SymbolTable:
    def __init__(self):
        self.symboltable = {}

    # string int -> __
    # adds new symbol/address pair to symbol table
    def addEntry(self, symbol, address):
        self.symboltable[symbol] = address

    # string -> boolean
    # checks to see if symbol is present in the table
    def contains(self, symbol):
        if symbol in self.symboltable:
            return true
        else:
            return false

    # string -> int
    # returns the address corresponding to the given symbol
    def getAddress(self, symbol):
        return self.symboltable[symbol]


if __name__ == "__main__":
    main()
