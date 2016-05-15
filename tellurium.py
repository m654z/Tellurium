import string, sys

tape = [0] * 25500
readingNum = False
readingIf = False
num = []
code = []
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
    global num
    global code
    global selected

    if readingNum == True:
        if cmd == "[":
            readingNum = False
            readingIf = True

        else:
            num.append(cmd)

    elif readingIf == True:
        if cmd == "]":
            readingIf = False
            if tape[selected] == int(''.join(num)):
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
        a = int(tape[selected])
        b = int(tape[selected+1])
        a += b

    elif cmd == "s":
        tape[selected] -= tape[selected+1]

    elif cmd == "m":
        tape[selected] *= tape[selected+1]

    elif cmd == "d":
        tape[selected] /= tape[selected+1]

    elif cmd == "(":
        readingNum = True

    elif cmd == "c":
        tape[selected] = tape[selected+1]

    elif cmd == "d":
        tape[selected] = tape[selected-1]

while 1:
    read(prompt())
