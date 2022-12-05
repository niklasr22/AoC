import aocutils

lines = aocutils.read_lines("./2022/inputs/day5.txt", ignore_empty_lines=False)

sep_line = lines.index("")

stack_count = int(lines[sep_line - 1].strip().split(" ")[-1])
stacks = [[] for _ in range(stack_count)]

stack_configuration = lines[: sep_line - 1]
for sl in reversed(stack_configuration):
    for i in range(stack_count):
        c = sl[1 + i * 4]
        if c != " ":
            stacks[i].append(c)

for c in lines[sep_line + 1 :]:
    count, c = c.split(" from ")
    count = int(count[5:])
    src, dest = c.split(" to ")
    src = int(src) - 1
    dest = int(dest) - 1

    stacks[dest] += stacks[src][len(stacks[src]) - count :]
    stacks[src] = stacks[src][: len(stacks[src]) - count]


print("".join([s[-1] for s in stacks]))
