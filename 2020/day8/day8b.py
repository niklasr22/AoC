from typing import Tuple

file = open("./2020/day8/input.txt")
data = file.read()

instructions = list(
    map(
        lambda y: [y[0], int(y[1]), 0],
        list(map(lambda x: x.split(" "), data.splitlines())),
    )
)


def checkProgram(instructions) -> Tuple[bool, int]:
    acc = 0
    i = instructions[0]
    x = 0
    l = len(instructions)
    t = False
    while i[2] == 0:
        i[2] += 1
        if i[0] == "jmp":
            x += i[1]
            if x >= l:
                t = True
                break
        elif i[0] == "nop":
            x += 1
            if x >= l:
                t = True
                break
        elif i[0] == "acc":
            acc += i[1]
            x += 1
            if x >= l:
                t = True
                break
        i = instructions[x]
    clearProgram(instructions)
    return t, acc


def clearProgram(instructions):
    for i in instructions:
        i[2] = 0


x = 0
for i in instructions:
    if i[0] == "jmp":
        i[0] = "nop"
        t, acc = checkProgram(instructions)
        if t:
            print(acc)
            break
        i[0] = "jmp"
    elif i[0] == "nop":
        i[0] = "jmp"
        t, acc = checkProgram(instructions)
        if t:
            print(acc)
            break
        i[0] = "nop"
    x += 1
