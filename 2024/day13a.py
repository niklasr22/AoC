import re
from pathlib import Path

data = Path("2024/inputs/day13.txt").read_text().strip()

machines = [
    (
        tuple(map(int, re.search(r"Button A: X\+(\d+), Y\+(\d+)", m).groups())),
        tuple(map(int, re.search(r"Button B: X\+(\d+), Y\+(\d+)", m).groups())),
        tuple(map(int, re.search(r"Prize: X=(\d+), Y=(\d+)", m).groups())),
    )
    for m in data.split("\n\n")
]


def can_win_a(m):
    (ax, ay), (bx, by), (px, py) = m

    spending = None
    for a in range(100):
        for b in range(100):
            if a * ax + b * bx == px and a * ay + b * by == py:
                if spending is None:
                    spending = a * 3 + b
                else:
                    spending = min(spending, a * 3 + b)
    return 0 if spending is None else spending


winnable = [can_win_a(m) for m in machines]
print(sum(winnable))
