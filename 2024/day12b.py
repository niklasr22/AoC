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


def find_sides(series):
    sides = 0
    ref = None

    for e in series:
        if ref is None:
            ref = e
            continue
        if ref == e:
            continue
        sides += abs(ref - e)
        ref = e
    return sides


price = 0
for cluster in clusters:
    area = len(cluster)

    min_x = min(x for y, x in cluster)
    min_y = min(y for y, x in cluster)
    width = max(x for y, x in cluster) - min_x + 1
    height = max(y for y, x in cluster) - min_y + 1

    cluster_grid = np.array(
        [
            [1 if (y + min_y, x + min_x) in cluster else 0 for x in range(width)]
            for y in range(height)
        ]
    )
    cluster_grid = np.pad(cluster_grid, 1, constant_values=0)

    # horizontal ray
    sides_vertical = 0
    ref = None
    for col in np.rot90(cluster_grid):
        if ref is None:
            ref = col
            continue

        diff = ref - col
        if (diff == 0).all():
            ref = col
            continue
        sides_vertical += find_sides(diff) // 2
        ref = col

    # vertical ray
    sides_horizontal = 0
    ref = None
    for row in cluster_grid:
        if ref is None:
            ref = row
            continue

        diff = ref - row
        if (diff == 0).all():
            ref = row
            continue
        sides_horizontal += find_sides(diff) // 2
        ref = row

    price += area * (sides_vertical + sides_horizontal)

print(price)
