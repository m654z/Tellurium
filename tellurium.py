import string
import sys
import random
import time
import codecs
import functools
import operator
import math
import statistics
import re

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
    "£": chr,
    "€": str,
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
readingModeAmount = False
readingRemove = False
commandSet2 = False
readingTimes = False
readingCount = False
readingLetter = False
readingNumber = False
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
ifThis = []
ifCode = []
mode = []
toRemove = []
times = []
count = []
letter = []
number = []
selected = 0
modeAmount = []
currentReturned = 0

def read(cmd):
    if isinstance(cmd, str):
        cmd = cmd.replace("!K", "1000")
        cmd = cmd.replace("!H", "100")
        cmd = cmd.replace("!a", "abcdefghijklmnopqrstuvwxyz")
        cmd = cmd.replace("!A", "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        cmd = cmd.replace("!D", "1234567890")
        cmd = cmd.replace("!O", "Hello, world!")
        cmd = cmd.replace("!o", "Hello, World!")
        cmd = cmd.replace("!P", "3.14159265359")
        cmd = cmd.replace("!E", "2.71828182846")
        cmd = cmd.replace("!I", "1.41421356237")
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
    global readingModeAmount
    global readingRemove
    global readingTimes
    global readingNumber
    global commandSet2
    global removing
    global tempName
    global tempText
    global readingLetter
    global fName
    global fCode
    global text
    global rand
    global rand2
    global selectingText
    global loopCode
    global loopAmount
    global readCode
    global ifThis
    global ifCode
    global mode
    global toRemove
    global selected
    global modeAmount
    global number
    global readingCount
    global times
    global count
    global letter
    global currentReturned

    if readingCount == True:
        if cmd == ".":
            readingCount = False
            currentReturned = str(tape[selected]).count(''.join(count))
            count = []

        else:
            count.append(cmd)

    if commandSet2 == True:
        if readingNumber == True:
            if cmd == ".":
                if str(type(tape[selected])) == "<class 'list'>":
                    newNum = int(re.sub("[^0-9]", "", ''.join(number)))
                    currentReturned = tape[selected][newNum]
                    number = []
                    commandSet2 = False

                else:
                    print("ListError: value is not a list.")

            else:
                number.append(cmd)

        else:
            number.append(cmd)
        if readingLetter == True:
            if cmd == ".":
                tape[selected] = []
                words = open('words.txt', 'r')
                wordList = list(words)
                wordList = map(lambda x: str.replace(x, "\n", ""), wordList)
                for w in wordList:
                    if w[0] == ''.join(letter):
                        tape[selected].append(w)

                commandSet2 = False

            else:
                letter.append(cmd)
                
        if readingTimes == True:
            if cmd == ".":
                readingTimes = False
                commandSet2 = False
                print(str(tape[selected])*int(''.join(times)))
                times = []

            else:
                times.append(cmd)
                
        elif cmd == "m":
            readingTimes = True

        elif cmd == "w":
            readingLetter = True

        elif cmd == "l":
            readingNumber = True

    elif readingModeAmount == True:
        if cmd == ".":
            currentSelected = selected
            for i in range(0, int(''.join(modeAmount))):
                selected += 1
                mode.append(tape[selected])

            selected = currentSelected
            tape[selected] = statistics.mode(mode)
            mode = []
            modeAmount = []

        elif cmd == ",":
            currentSelected = selected
            for i in range(0, int(''.join(modeAmount))):
                selected += 1
                mode.append(tape[selected])

            selected = currentSelected
            tape[selected] = statistics.median(mode)
            mode = []
            modeAmount = []

        elif cmd == ";":
            currentSelected = selected
            for i in range(0, int(''.join(modeAmount))):
                selected += 1
                mode.append(tape[selected])

            selected = currentSelected
            tape[selected] = statistics.mean(mode)
            mode = []
            modeAmount = []

        else:
            modeAmount.append(cmd)

    elif readingLoopAmount == True:
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
        if cmd == ";":
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
        if readingRemove == True:
            if cmd == "~":
                tape[selected] = str(tape[selected]).replace(''.join(toRemove), "")
                readingRemove = False
                toRemove = []

            else:
                toRemove.append(cmd)
                
        elif appendToFront == True:
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
            try:
                tape[selected] = tape[selected][::-1]

            except TypeError:
                tape[selected] = str(tape[selected])[::-1]

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

        elif cmd == "x":
            readingRemove = True

        elif cmd == "s":
            tape[selected] = re.sub(r"(\w)([A-Z])", r"\1 \2", str(tape[selected]))

        elif cmd == "j":
            tape[selected] = ''.join(tape[selected])

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
        try:
            tape[selected] = op(int(tape[selected]), int(tape[selected + 1]))

        except ZeroDivisionError:
            print("ZeroDivisonError: can't divide by zero.")

    elif cmd in POSITION_ACTIONS:
        selected = POSITION_ACTIONS[cmd](selected)

    elif cmd == "½":
        tape[selected] = math.exp(tape[selected])

    elif cmd == "§":
        try:
            tape[selected] = math.factorial(tape[selected])

        except ValueError:
            print("ValueError: can't calculate the factorial of " + str(tape[selected]) + ".")

    elif cmd == "q":
        try:
            tape[selected] = math.sqrt(tape[selected])

        except ValueError:
            print("ValueError: can't calculate the square root of " + str(tape[selected]) + ".")

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

    elif cmd == "\u2192":
        if rand != []:
            rand = []

        readingRand = True

    elif cmd == "\u2190":
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
        currentReturned = fib(tape[selected])

    elif cmd == "T":
        if str(type(tape[selected])) == "<class 'str'>":
            print("String")

        elif str(type(tape[selected])) == "<class 'int'>":
            print("Integer")

        elif str(type(tape[selected])) == "<class 'float'>":
            print("Float")

        elif str(type(tape[selected])) == "<class 'list'>":
            print("List")

        else:
            print("Other")

    elif cmd == "?":
        readingIf = True

    elif cmd == "P":
        if isPrime(tape[selected]):
            currentReturned = 1

        else:
            currentReturned = 0

    elif cmd == "E":
        read(tape[selected])

    elif cmd == "L":
        tape[selected] = len(str(tape[selected]))

    elif cmd == "G":
        graphics = True

    elif cmd == "M":
        readingModeAmount = True

    elif cmd == "ö":
        tape[selected] = currentReturned

    elif cmd == "Ö":
        print(currentReturned)

    elif cmd == "Å":
        commandSet2 = True

    elif cmd == "C":
        readingCount = True

    elif cmd == "b":
        if tape[selected-1] > tape[selected]:
            tape[selected+1] = 1

        else:
            tape[selected+1] = 0

    elif cmd == "l":
        if tape[selected-1] < tape[selected]:
            tape[selected+1] = 1

        else:
            tape[selected+1] = 0

    elif cmd == "U":
        if tape[selected-1] == tape[selected]:
            tape[selected+1] = 1

        else:
            tape[selected+1] = 0

    elif cmd in "1234567890":
        tape[selected] += int(cmd)
    
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
        try:
            parser_stack.pop()
            tape[selected] = variables[''.join(vName2)]
            vName2 = []

        except KeyError:
            print("VariableError: No such variable named " + ''.join(vName2) + ".")

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

def isPrime(n):
    trueFalse = all(n % i for i in range(2, n))
    if trueFalse == True:
        return(1)

    else:
        return(0)

def parse(token):
    return parser_stack[-1](token)

while 1:
    read(input("> "))
