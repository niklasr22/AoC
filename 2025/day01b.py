from pathlib import Path

data = Path("2025/inputs/day01.txt").read_text().strip()

lines = data.splitlines()

instr = list(map(lambda l: (l[0], int(l[1:])), lines))

current = 50
zeros = 0

for dir, no in instr:
    f = -1 if dir == "L" else 1
    new = (current + f * no) % 100
    rest = current if dir == "L" else 100 - current
    iter_zeros = no // 100 + (
        1 if (no - (100 * (no // 100))) >= rest and current != 0 else 0
    )
    current = new
    zeros += iter_zeros

print(zeros)
