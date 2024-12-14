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

time = 100
quadrants = [0, 0, 0, 0]
for bot in bots:
    pos_after = (bot[:2] + bot[2:] * time) % (width, height)
    if pos_after[0] < width // 2:
        if pos_after[1] < height // 2:
            quadrants[0] += 1
        elif pos_after[1] > height // 2:
            quadrants[1] += 1
    elif pos_after[0] > width // 2:
        if pos_after[1] < height // 2:
            quadrants[2] += 1
        elif pos_after[1] > height // 2:
            quadrants[3] += 1
print(quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3])
