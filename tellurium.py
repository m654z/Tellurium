import string, sys, random

tape = [0] * 25500
readingNum = False
readingIf = False
readingStr = False
readingLoopAmount = False
readingLoopCode = False
readingRand = False
readingRand2 = False
loopInf = False
loopRand = False
string = False
isChar = False
num = []
code = []
text = []
rand = []
rand2 = []
loopCode = []
loopAmount = []
selected = 0

def prompt():
    cmd = input("> ")
    return cmd

def read(cmd):
    commands = len(cmd)
    tokens = list(cmd)
    for i in range(0, commands):
        parse(tokens[i])

def parse(cmd):
    global tape
    global readingNum
    global readingIf
    global readingStr
    global readingLoopAmount
    global readingLoopCode
    global readingRand
    global readingRand2
    global loopInf
    global loopRand
    global string
    global isChar
    global num
    global code
    global text
    global rand
    global rand2
    global loopCode
    global loopAmount
    global selected

    if readingRand == True:
        if cmd == "|":
            readingRand = False

        else:
            rand.append(cmd)

    if readingRand2 == True:
        if cmd == "|":
            readingRand2 = False

        else:
            rand2.append(cmd)

    elif string == True:
        if cmd == "r":
            tape[selected] = tape[selected].reverse()

        if cmd == "u":
            tape[selected] = tape[selected].upper()

        if cmd == "l":
            tape[slected] = tape[selected].lower()

        if cmd == ".":
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

    elif readingNum == True:
        if cmd == "[":
            readingNum = False
            readingIf = True

        else:
            if isinstance(cmd, str):
                isChar = True

            elif cmd.isdigit():
                cmd = int(cmd)
                
            num.append(cmd)

    elif readingIf == True:
        if cmd == "]":
            readingIf = False
            if isChar == True:
                if [selected] == ''.join(num):
                    read(code)
                    code = []
                    num = []
                    isChar = False

                else:
                    return
                
            elif tape[selected] == int(''.join(num)):
                read(code)
                code = []
                num = []

            else:
                return

        else:
            code.append(cmd)
    
    elif cmd == "+":
        tape[selected] += 1

    elif cmd == "-":
        tape[selected] -= 1

    elif cmd == ">":
        selected += 1

    elif cmd == "<":
        selected -= 1

    elif cmd == "*":
        print(selected)

    elif cmd == "^":
        print(tape[selected])

    elif cmd == "!":
        if isinstance(tape[selected], str):
            print(tape[selected])
        else:
            print(chr(tape[selected]))

    elif cmd == "%":
        tape[selected] = ord(tape[selected])

    elif cmd == "#":
        tape[selected] = 0

    elif cmd == "$":
        selected = 0

    elif cmd == "/":
        tape[selected] += 10

    elif cmd == "\\":
        tape[selected] -= 10

    elif cmd == "{":
        selected += 10

    elif cmd == "}":
        selected -= 10

    elif cmd == '"':
        tape[selected] += 100

    elif cmd == "'":
        tape[selected] -= 100

    elif cmd == "-":
        selected += 100

    elif cmd == "_":
        selected -= 100

    elif cmd == "i":
        tape[selected] = input(">> ")

    elif cmd == "n":
        tape[selected] = int(tape[selected])

    elif cmd == "a":
        tape[selected] = int(tape[selected]) + int(tape[selected+1])

    elif cmd == "s":
        tape[selected] = int(tape[selected]) - int(tape[selected+1])

    elif cmd == "m":
        tape[selected] = int(tape[selected]) * int(tape[selected+1])

    elif cmd == "d":
        tape[selected] = int(tape[selected]) / int(tape[selected+1])

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

while 1:
    read(prompt())
