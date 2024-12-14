import re
from pathlib import Path

import numpy as np

bots = np.array(
    list(
        map(
            int,
            re.findall(
                r"(-{0,1}\d+)", Path("2024/inputs/day14.txt").read_text().strip()
            ),
        )
    )
).reshape(-1, 4)

width = 101
height = 103

time = 1
while True:

    grid = np.zeros((height, width))
    check = False
    for bot in bots:
        pos_after = (bot[:2] + bot[2:] * time) % (width, height)
        grid[pos_after[1], pos_after[0]] += 1

    for row in grid:
        line = "".join(map(lambda r: "#" if r > 0 else " ", row))
        # heuristic to check if there are many bots in a straight line without gaps
        if "#" * 10 in line:
            check = True

    if check:
        print("Candidate found:")
        for row in grid:
            print("".join(map(lambda r: "#" if r > 0 else " ", row)))
        print(time)
        time += 1
        a = input()
        if a.isnumeric():
            time = int(a)
    else:
        print(time)
        time += 1
