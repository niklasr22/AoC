import math
from pathlib import Path

import networkx as nx

grid = Path("2023/inputs/day21_sm.txt").read_text().splitlines()

G = nx.Graph()

width = len(grid[0])
height = len(grid)
adjacents = [(0, 1), (0, -1), (1, 0), (-1, 0)]
edges = []
start = None
target = None
for y in range(height):
    for x in range(width):
        if grid[y][x] == "#":
            continue
        elif grid[y][x] == "S":
            start = (x, y)
        elif grid[y][x] == "X":
            target = (x, y)
        for o_x, o_y in adjacents:
            n_x = x + o_x
            n_y = y + o_y
            if 0 <= n_x < width and 0 <= n_y < height:
                if grid[n_y][n_x] != "#":
                    edges.append(((x, y), (n_x, n_y), 1))

visited = set()
queue = {start}
final_spots = set()
print("start", start)

uneven_steps = False

reference = queue.copy()
steps_for_ref = 0
steps = 0
while True:
    new_queue = set()
    for x, y in queue:
        for o_x, o_y in adjacents:
            n_x = x + o_x
            n_y = y + o_y
            if 0 <= n_x < width and 0 <= n_y < height:
                # print(n_x, n_y, grid[n_y][n_x], grid[n_y])
                if grid[n_y][n_x] != "#":
                    new_queue.add((n_x, n_y))
    starting_points = queue
    queue = new_queue

    steps += 1
    uneven_steps = not uneven_steps

    if uneven_steps:
        if queue != reference:
            reference = queue
            steps_for_ref = steps
        else:
            print(steps_for_ref + 1)
            break
