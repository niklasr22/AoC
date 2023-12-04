from collections import defaultdict

import aocutils

grid = aocutils.read_lines("./2022/inputs/day12.txt")

pos_x = -1
pos_y = -1
target_x = -1
target_y = -1
height = len(grid)
width = len(grid[0])

a_positions = []
for y, row in enumerate(grid):
    grid[y] = list(row)
    for x, c in enumerate(row):
        if c == "S":
            pos_x = x
            pos_y = y
            grid[y][x] = ord("z")
            a_positions.append((x, y))
        elif c == "E":
            target_x = x
            target_y = y
            grid[y][x] = ord("z")
        else:
            if grid[y][x] == "a":
                a_positions.append((x, y))
            grid[y][x] = ord(grid[y][x])

grid = {(x, y): grid[y][x] for x in range(width) for y in range(height)}
nodes = set(grid.keys())


def neighbours(n) -> list:
    x, y = n
    return [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]


def dist(u, v) -> float:
    return 1 if grid[u] - grid[v] <= 1 else float("inf")


distances, _ = aocutils.dijkstra(nodes, (target_x, target_y), neighbours, dist)
print(min([d for (x, y), d in distances.items() if (x, y) in a_positions]))
