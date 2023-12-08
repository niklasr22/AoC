import functools
from pathlib import Path


def kgv(numbers: list[int]) -> list[int]:
    return functools.reduce(lambda a, b: a * b // ggt([a, b]), numbers)


def ggt(numbers: list[int]) -> list[int]:
    for i in range(0, len(numbers) - 1):
        while numbers[1]:
            numbers[0], numbers[1] = numbers[1], numbers[0] % numbers[1]
        numbers[1] = numbers[i + 1]
    return numbers[0]


instr = Path("2023/inputs/day8.txt").read_text().splitlines()


rl_instr = instr[0]


net = {
    line.split(" = ")[0]: line.split(" = (")[1][:-1].split(", ") for line in instr[2:]
}


def get_steps_for_start(pos, net, rl_instr):
    i = 0
    steps = 0
    while not pos.endswith("Z"):
        turn = 0 if rl_instr[i] == "L" else 1
        pos = net[pos][turn]
        i = (i + 1) % len(rl_instr)
        steps += 1
    return steps


positions = [pos for pos in net.keys() if pos.endswith("A")]

steps = []
for pos in positions:
    steps.append(get_steps_for_start(pos, net, rl_instr))

print(kgv(steps))
