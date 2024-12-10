from pathlib import Path

import numpy as np

data = Path("2024/inputs/day10.txt").read_text().strip()

grid = np.array(
    [
        list(map(lambda x: -1000 if x == "." else int(x), list(row)))
        for row in data.splitlines()
    ]
)

offsets = [np.array([0, 1]), np.array((1, 0)), np.array((0, -1)), np.array((-1, 0))]


def move(pos):
    if grid[*pos] == 9:
        return 1

    score = 0
    for offset in offsets:
        new_pos = pos + offset
        if not (0 <= new_pos[0] < len(grid) and 0 <= new_pos[1] < len(grid[0])):
            continue
        if grid[*new_pos] - grid[*pos] == 1:
            score += move(new_pos)
    return score


score_sum = 0

trailheads = np.argwhere(grid == 0)
for trailhead in trailheads:
    score_sum += move(trailhead)
print(score_sum)
