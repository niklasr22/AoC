from pathlib import Path

import numpy as np

data = Path("2024/inputs/day12.txt").read_text().strip().splitlines()

grid = np.pad(np.array([list(row) for row in data]), 1, constant_values=".")

seen = set()

clusters = []

offsets = [np.array((0, 1)), np.array((0, -1)), np.array((1, 0)), np.array((-1, 0))]


def dfs(pos: np.array, cluster: set):
    if tuple(pos) in seen:
        return
    seen.add(tuple(pos.tolist()))
    val = grid[*pos]
    cluster.add(tuple(pos.tolist()))

    for offset in offsets:
        new_pos = pos + offset
        new_val = grid[*new_pos]
        if new_val == val:
            dfs(new_pos, cluster)


for i in range(1, grid.shape[0] - 1):
    for j in range(1, grid.shape[1] - 1):
        if (i, j) not in seen:
            clusters.append(set())
            dfs(np.array((i, j)), clusters[-1])

price = 0
for cluster in clusters:
    area = len(cluster)

    perimeter = 0

    for pos in cluster:
        for offset in offsets:
            new_pos = np.array(pos) + offset
            if tuple(new_pos) not in cluster:
                perimeter += 1

    price += area * perimeter

print(price)
