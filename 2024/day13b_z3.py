import math
import re
from pathlib import Path

import z3

data = Path("2024/inputs/day13.txt").read_text().strip()

machines = [
    (
        tuple(map(int, re.search(r"Button A: X\+(\d+), Y\+(\d+)", m).groups())),
        tuple(map(int, re.search(r"Button B: X\+(\d+), Y\+(\d+)", m).groups())),
        tuple(map(int, re.search(r"Prize: X=(\d+), Y=(\d+)", m).groups())),
    )
    for m in data.split("\n\n")
]


def can_win_b(m):
    (ax, ay), (bx, by), (px, py) = m

    px += 10000000000000
    py += 10000000000000

    a = z3.Int("A")
    b = z3.Int("B")
    s = z3.Solver()

    s.add(
        a >= 0,
        b >= 0,
        a * ax + b * bx == px,
        a * ay + b * by == py,
    )
    if s.check() == z3.unsat:
        return 0

    def cost(a, b):
        return a * 3 + b

    return s.model().eval(cost(a, b)).as_long()


winnable = [can_win_b(m) for m in machines]
print(sum(winnable))
