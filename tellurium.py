import string
import sys
import random
import time
import codecs
import functools
import operator

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
readingSkip = False
readingStr = False
readingLoopAmount = False
readingLoopCode = False
readingRand = False
readingRand2 = False
readingFName = False
readingFCode = False
appendToFront = False
appendToBack = False
loopInf = False
loopRand = False
string = False
isChar = False
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
selected = 0

def read(cmd):
    if isinstance(cmd, str):
        cmd = cmd.replace("!K", "1000")
        cmd = cmd.replace("!H", "100")
        cmd = cmd.replace("´", "\n")

    for token in cmd:
        parse(token)

def _parse(cmd):
    global tape
    global funcs
    global variables
    global readingStr
    global readingSkip
    global readingLoopAmount
    global readingLoopCode
    global readingRand
    global readingRand2
    global readingFName
    global readingFCode
    global appendToFront
    global appendToBack
    global loopInf
    global loopRand
    global vName, vText
    global fileName
    global string
    global isChar
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
    global selected

    if readingSkip == True:
        if cmd == "}":
            readingSkip = False
            if tape[selected] == 0:
                return

            elif tape[selected] != 0:
                read(code)
                code = []

        else:
            code.append(cmd)

    if readingFName == True:
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

        elif cmd == ".":
            string = False

    elif readingLoopAmount == True:
        if cmd == "|":
            readingLoopAmount = False
            readingLoopCode = True

        elif cmd == "i":
            loopInf = True

        elif cmd == "r":
            loopRand = True

        else:
            loopAmount.append(cmd)

    elif readingLoopCode == True:
        if cmd == "]":
            readingLoopCode = False
            if loopInf == True:
                while 1:
                    read(loopCode)

            if loopRand == True:
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

            else:
                for i in range(0, int(''.join(loopAmount))):
                    read(loopCode)

            loopCode = []
            loopAmount = []

        else:
            loopCode.append(cmd)

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

    elif cmd == "{":
        readingSkip = True


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

def parse(token):
    return parser_stack[-1](token)

while 1:
    read(input("> "))
