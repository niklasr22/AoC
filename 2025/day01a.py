from pathlib import Path

data = Path("2025/inputs/day01.txt").read_text().strip()

lines = data.splitlines()

instr = list(map(lambda l: (l[0], int(l[1:])), lines))

current = 50

zeros = 0

for dir, no in instr:
    f = -1 if dir == "L" else 1
    current = (current + f * no) % 100
    if current == 0:
        zeros += 1

print(zeros)
