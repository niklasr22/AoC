import aocutils

lines = aocutils.read_lines("./2022/inputs/day5.txt")

first_move_line = 0
for l in lines:
    if l.startswith("m"):
        break
    first_move_line += 1

stack_configuration = lines[: first_move_line - 1]
stack_count = int(lines[first_move_line - 1].strip().split(" ")[-1])
stacks = [list() for _ in range(stack_count)]

for sl in reversed(stack_configuration):
    print(sl)
    for i in range(stack_count):
        c = sl[1 + i * 4]
        if c != " ":
            stacks[i].append(c)

print(stacks)

commands = lines[first_move_line:]

for c in commands:
    count, c = c.split(" from ")
    count = int(count[5:])
    src, dest = c.split(" to ")
    src = int(src) - 1
    dest = int(dest) - 1
    for i in range(count):
        x = stacks[src].pop()
        stacks[dest].append(x)


print("".join([s[-1] for s in stacks]))
