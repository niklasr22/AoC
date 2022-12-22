import aocutils
from collections import defaultdict

grid = aocutils.read_lines("./2022/inputs/day12.txt")

pos_x = -1
pos_y = -1
target_x = -1
target_y = -1
height = len(grid)
width = len(grid[0])

for y, row in enumerate(grid):
    grid[y] = list(row)
    for x, c in enumerate(row):
        if c == "S":
            pos_x = x
            pos_y = y
            grid[y][x] = ord("z")
        elif c == "E":
            target_x = x
            target_y = y
            grid[y][x] = ord("z")
        else:
            grid[y][x] = ord(grid[y][x])

grid = {(x, y): grid[y][x] for x in range(width) for y in range(height)}
nodes = set(grid.keys())


def neighbours(n) -> list:
    x, y = n
    return [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]


def dist(u, v) -> float:
    return 1 if grid[v] - grid[u] <= 1 else float("inf")


distances, _ = aocutils.dijkstra(
    nodes, (pos_x, pos_y), neighbours, dist, (target_x, target_y)
)
print(distances[(target_x, target_y)])
