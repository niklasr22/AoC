import math
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

    min_x = min(x for _, x in cluster)
    min_y = min(y for y, _ in cluster)
    width = max(x for _, x in cluster) - min_x + 1
    height = max(y for y, _ in cluster) - min_y + 1

    cluster_grid = np.array(
        [
            [1 if (y + min_y, x + min_x) in cluster else 0 for x in range(width)]
            for y in range(height)
        ]
    )
    cluster_grid = np.pad(cluster_grid, 1, constant_values=0)

    sides = 0
    comp_kernel = np.array([[0, 0, 0], [0, 0, 1], [0, 1, 1]])
    comp_kernel_out = np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0]])
    for y in range(1, height + 1):
        for x in range(1, width + 1):
            for i in range(4):
                if cluster_grid[y, x] == 1:
                    neighbors = np.sum(
                        comp_kernel * cluster_grid[y - 1 : y + 2, x - 1 : x + 2]
                    )
                    if neighbors == 0:
                        sides += 1
                    comp_kernel = np.rot90(comp_kernel)
                else:
                    neighbors = np.sum(
                        comp_kernel_out * cluster_grid[y - 1 : y + 2, x - 1 : x + 2]
                    )
                    if neighbors == 2:
                        sides += 1
                    comp_kernel_out = np.rot90(comp_kernel_out)

    price += area * sides

print(price)
