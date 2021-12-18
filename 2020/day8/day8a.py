file = open("./2020/day8/input.txt")
data = file.read()

instructions = list(map(lambda y: [y[0], int(y[1]), 0], list(map(lambda x : x.split(" "), data.splitlines()))))

acc = 0
i = instructions[0]
x = 0
l = len(instructions)
while i[2] == 0:
    i[2] += 1
    if i[0] == "jmp":
        x += i[1]
    elif i[0] == "nop":
        x += 1
    elif i[0] == "acc":
        acc += i[1]
        x += 1
    i = instructions[x]
print(acc)