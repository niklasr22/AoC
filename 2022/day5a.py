import aocutils

lines = aocutils.read_lines("./2022/inputs/day5.txt", ignore_empty_lines=False)

sep_line = lines.index("")

stack_count = int(lines[sep_line - 1].strip().split(" ")[-1])
stacks = [[] for _ in range(stack_count)]

stack_configuration = lines[: sep_line - 1]
for sl in reversed(stack_configuration):
    for i in range(stack_count):
        crate = sl[1 + i * 4]
        if crate != " ":
            stacks[i].append(crate)

for cmd in lines[sep_line + 1 :]:
    count, cmd = cmd.split(" from ")
    count = int(count[5:])
    src, dest = cmd.split(" to ")
    src = int(src) - 1
    dest = int(dest) - 1
    for i in range(count):
        x = stacks[src].pop()
        stacks[dest].append(x)


print("".join([s[-1] for s in stacks]))
