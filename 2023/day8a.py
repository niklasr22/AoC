from pathlib import Path

instr = Path("2023/inputs/day8.txt").read_text().splitlines()


rl_instr = instr[0]


net = {
    line.split(" = ")[0]: line.split(" = (")[1][:-1].split(", ") for line in instr[2:]
}

pos = "AAA"
i = 0
steps = 0
while pos != "ZZZ":
    turn = 0 if rl_instr[i] == "L" else 1
    pos = net[pos][turn]
    i = (i + 1) % len(rl_instr)
    steps += 1

print(steps)
