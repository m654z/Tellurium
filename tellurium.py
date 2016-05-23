import string
import sys
import random
import time
import codecs
import functools
import operator
import math

INT_BINOPS = {
    "a": operator.add,
    "s": operator.sub,
    "m": operator.mul,
    "d": operator.truediv,
}
    
INPLACE_UNARYOPS = {
    "+": functools.partial(operator.add, 1),
    "-": functools.partial(operator.add, -1),
    "/": functools.partial(operator.add, 10),
    "\\": functools.partial(operator.add, -10),
    '"': functools.partial(operator.add, 100),
    "'": functools.partial(operator.add, -100),
    "n": int,
    "f": float,
    "%": ord,
    "r": lambda v: codecs.encode(str(v), 'rot_13'),
}

FUNCS = {
    "t": lambda: str(time.ctime()),
    "#": lambda: 0,
    "i": lambda: input(">> "),
}

POSITION_ACTIONS = {
    "$": lambda _: 0,
    ">": functools.partial(operator.add, 1),
    "<": functools.partial(operator.add, -1),
    "e": functools.partial(operator.add, 10),
    "E": functools.partial(operator.add, -10),
    "h": functools.partial(operator.add, 100),
    "H": functools.partial(operator.add, -100),
}

tape = [0] * 25500
funcs = {}
variables = {}
readingStr = False
readingLoopAmount = False
readingLoopCode = False
readingIfCode = False
readingRand = False
readingRand2 = False
readingFName = False
readingFCode = False
readingCode = False
appendToFront = False
appendToBack = False
readingIf = False
loopInf = False
loopRand = False
loopInp = False
loopLen = False
string = False
isChar = False
ifInt = False
ifStr = False
ifFloat = False
vName = []
vName2 = []
vText = []
fileName = []
tempText = []
tempName = []
fName = []
fCode = []
text = []
rand = []
rand2 = []
code = []
loopCode = []
loopAmount = []
readCode = []
ifThis = []
ifCode = []
selected = 0

def read(cmd):
    if isinstance(cmd, str):
        cmd = cmd.replace("!K", "1000")
        cmd = cmd.replace("!H", "100")
        cmd = cmd.replace("!a", "abcdefghijklmnopqrstuvwxyz")
        cmd = cmd.replace("!A", "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        cmd = cmd.replace("!D", "1234567890")
        cmd = cmd.replace("´", "\n")

    for token in cmd:
        parse(token)

def _parse(cmd):
    global tape
    global funcs
    global variables
    global readingStr
    global readingLoopAmount
    global readingLoopCode
    global readingRand
    global readingRand2
    global readingFName
    global readingFCode
    global readingCode
    global readingIf
    global readingIfCode
    global appendToFront
    global appendToBack
    global loopInf
    global loopRand
    global loopInp
    global loopLen
    global vName, vText
    global fileName
    global string
    global isChar
    global ifInt
    global ifStr
    global ifFloat
    global removing
    global tempName
    global tempText
    global fName
    global fCode
    global text
    global rand
    global rand2
    global code
    global loopCode
    global loopAmount
    global readCode
    global ifThis
    global ifCode
    global selected

    if readingLoopAmount == True:
        if cmd == "|":
            readingLoopAmount = False
            readingLoopCode = True

        elif cmd == "i":
            loopInf = True

        elif cmd == "r":
            loopRand = True

        elif cmd == "I":
            loopInp = True

        elif cmd == "l":
            loopLen = True

        else:
            loopAmount.append(cmd)

    elif readingLoopCode == True:
        if cmd == "]":
            readingLoopCode = False
            
            if loopInf == True:
                while 1:
                    read(loopCode)

            elif loopRand == True:
                if rand and rand2 == []:
                    for i in range(0, random.randint(0, 100)):
                        read(loopCode)

                else:
                    if rand2 == []:
                        for i in range(0, random.randint(0, int(''.join(rand)))):
                            read(loopCode)

                    elif rand == []:
                        for i in range(0, random.randint(int(''.join(rand2)), 100)):
                            read(loopCode)

                    else:
                        for i in range(0, random.randint(int(''.join(rand2)), int(''.join(rand)))):
                            read(loopCode)

            elif loopInp == True:
                for i in range(0, int(input((">> ")))):
                    read(loopCode)

            elif loopLen == True:
                for i in range(0, len(tape[selected])):
                    read(loopCode)

            else:
                for i in range(0, int(''.join(loopAmount))):
                    read(loopCode)

            loopCode = []
            loopAmount = []

        else:
            loopCode.append(cmd)

    elif readingIf == True:
        if cmd == "|":
            readingIf = False
            readingIfCode = True

        else:
            ifThis.append(cmd)

    elif readingIfCode == True:
        if cmd == "]":
            readingIfCode = False
            ifT = ''.join(ifThis)
            if ifT.isdigit():
                ifT = int(ifT)

            if tape[selected] == ifT:
                read(''.join(ifCode))

            ifCode = []
            ifThis = []

        else:
            ifCode.append(cmd)

    elif readingCode == True:
        if cmd == "€":
            readingCode = False
            tape[selected+1] = ''.join(readCode)
            readCode = []

        else:
            readCode.append(cmd)

    elif readingFName == True:
        if cmd == "|":
            readingFName = False
            readingFCode = True

        else:
            fName.append(cmd)

    elif readingFCode == True:
        if cmd == "`":
            readingFCode = False
            name = ''.join(fName)
            code = ''.join(fCode)
            funcs[name] = code
            fName = []
            fCode = []

        else:
            fCode.append(cmd)

    elif readingRand == True:
        if cmd == "|":
            readingRand = False

        else:
            rand.append(cmd)

    elif readingRand2 == True:
        if cmd == "|":
            readingRand2 = False

        else:
            rand2.append(cmd)

    elif string == True:
        if appendToFront == True:
            if cmd == "~":
                tape[selected] = str(tape[selected]) + ''.join(tempText)
                tempText = []
                appendToFront = False

            elif cmd == "$":
                tape[selected] = str(tape[selected]) + str(tape[selected-1])
                appendToFront = False
                tempText = []

            else:
                tempText.append(cmd)

        elif appendToBack == True:
            if cmd == "~":
                tape[selected] = ''.join(tempText) + str(tape[selected])
                tempText = []
                appendToBack = False

            elif cmd == "$":
                tape[selected] = str(tape[selected-1]) + str(tape[selected])
                appendToFront = False
                tempText = []

            else:
                tempText.append(cmd)

        elif cmd == "r":
            tape[selected] = tape[selected].reverse()

        elif cmd == "u":
            tape[selected] = tape[selected].upper()

        elif cmd == "l":
            tape[selected] = tape[selected].lower()

        elif cmd == "a":
            appendToFront = True

        elif cmd == "b":
            appendToBack = True

        elif cmd == "t":
            tape[selected] = str.title(tape[selected])

        elif cmd == "c":
            tape[selected] = str.capitalize(tape[selected])

        elif cmd == ".":
            string = False

    elif readingStr == True:
        if cmd == "~":
            readingStr = False
            text = ''.join(text).replace("µ", "")
            tape[selected] = text
            text = []

        else:
            text.append(cmd)

    elif cmd == "*":
        print(selected)

    elif cmd == "^":
        print(tape[selected])

    elif cmd == "!":
        if isinstance(tape[selected], str):
            print(tape[selected])
        else:
            print(chr(tape[selected]))

    elif cmd in FUNCS:
        tape[selected] = FUNCS[cmd]()

    elif cmd in INPLACE_UNARYOPS:
        op = INPLACE_UNARYOPS[cmd]
        tape[selected] = op(tape[selected])

    elif cmd in INT_BINOPS:
        op = INT_BINOPS[cmd]
        tape[selected] = op(int(tape[selected]), int(tape[selected + 1]))

    elif cmd in POSITION_ACTIONS:
        selected = POSITION_ACTIONS[cmd](selected)

    elif cmd == "½":
        tape[selected] = math.exp(tape[selected])

    elif cmd == "§":
        tape[selected] = math.factorial(tape[selected])

    elif cmd == "q":
        tape[selected] = math.sqrt(tape[selected])

    elif cmd == "c":
        tape[selected] = math.ceil(tape[selected])

    elif cmd == "g":
        tape[selected] = math.floor(tape[selected])

    elif cmd == "S":
        tape[selected] *= tape[selected]

    elif cmd == "(":
        readingNum = True

    elif cmd == "z":
        tape[selected] = tape[selected+1]

    elif cmd == "x":
        tape[selected] = tape[selected-1]

    elif cmd == "µ":
        readingStr = True

    elif cmd == "[":
        readingLoopAmount = True

    elif cmd == "p":
        return

    elif cmd == ".":
        exit

    elif cmd == "&":
        string = True

    elif cmd == "→":
        if rand != []:
            rand = []

        readingRand = True

    elif cmd == "←":
        if rand2 != []:
            rand2 = []

        readingRand2 = True

    elif cmd == "¨":
        time.sleep(1)

    elif cmd == "@":
        readingFName = True

    elif cmd == "=":
        parser_stack.append(read_name)
    elif cmd == "¤":
        parser_stack.append(read_vname)
    elif cmd == ";":
        parser_stack.append(read_vname2)
    elif cmd == "0":
        parser_stack.append(read_filename)

    elif cmd == "I":
        tape[selected] = int(input(">> "))

    elif cmd == "F":
        tape[selected+1] = fib(tape[selected])

    elif cmd == "T":
        if str(type(tape[selected])) == "<class 'str'>":
            print("String")

        elif str(type(tape[selected])) == "<class 'int'>":
            print("Integer")

        elif str(type(tape[selected])) == "<class 'float'>":
            print("Float")

        else:
            print("Other")

    elif cmd == "£":
        readingCode = True

    elif cmd == "?":
        readingIf = True

parser_stack = [_parse]


def read_name(cmd):
    global tempName
    if cmd == ".":
        parser_stack.pop()
        name = ''.join(tempName)
        read(funcs[name])
        tempName = []
    else:
        tempName.append(cmd)


def read_vtext(cmd):
    global vName, vText
    if cmd == "]":
        parser_stack.pop()
        name = ''.join(vName)
        val = ''.join(vText)
        variables[name] = val
        vName = []
        vText = []
    else:
        vText.append(cmd)


def read_vname(cmd):
    global vName
    if cmd == "|":
        parser_stack.pop()
        parser_stack.append(read_vtext)
    else:
        vName.append(cmd)


def read_vname2(cmd):
    global vName2
    if cmd == ".":
        parser_stack.pop()
        tape[selected] = variables[''.join(vName2)]
        vName2 = []

    else:
        vName2.append(cmd)



def read_filename(cmd):
    global fileName
    if cmd == "]":
        parser_stack.pop()
        f = open(''.join(fileName), 'r')
        code = f.read()
        f.close()
        read(code)
        fileName = []

    else:
        fileName.append(cmd)

def fib(n):
    a, b = 1, 1
    for i in range(n-1):
        a, b = b, a+b

    return a

def parse(token):
    return parser_stack[-1](token)

while 1:
    read(input("> "))
