import string, sys, random, time, codecs

tape = [0] * 25500
funcs = {}
readingStr = False
readingLoopAmount = False
readingLoopCode = False
readingRand = False
readingRand2 = False
readingFName = False
readingFCode = False
readingName = False
appendToFront = False
appendToBack = False
loopInf = False
loopRand = False
string = False
isChar = False
tempText = []
tempName = []
fName = []
fCode = []
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
    if "!K" in cmd:
        cmd = cmd.replace("!K", "1000")

    if "!H" in cmd:
        cmd = cmd.replace("!H", "100")
        
    commands = len(cmd)
    tokens = list(cmd)
    for i in range(0, commands):
        parse(tokens[i])

def parse(cmd):
    global tape
    global funcs
    global readingStr
    global readingLoopAmount
    global readingLoopCode
    global readingRand
    global readingRand2
    global readingFName
    global readingFCode
    global readingName
    global appendToFront
    global appendToBack
    global loopInf
    global loopRand
    global string
    global isChar
    global tempName
    global tempText
    global fName
    global fCode
    global text
    global rand
    global rand2
    global loopCode
    global loopAmount
    global selected

    if readingName == True:
        if cmd == ".":
            readingName = False
            name = ''.join(tempName)
            read(funcs[name])
            tempName = []

        else:
            tempName.append(cmd)

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

            else:
                tempText.append(cmd)

        elif appendToBack == True:
            if cmd == "~":
                tape[selected] = ''.join(tempText) + str(tape[selected])
                tempText = []
                appendToBack = False

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

    elif cmd == "t":
        tape[selected] = str(time.ctime())

    elif cmd == "¨":
        time.sleep(1)

    elif cmd == "r":
        tape[selected] = codecs.encode(str(tape[selected]), 'rot_13')

    elif cmd == "n":
        tape[selected] = int(tape[selected])

    elif cmd == "@":
        readingFName = True

    elif cmd == "=":
        readingName = True

while 1:
    read(prompt())
