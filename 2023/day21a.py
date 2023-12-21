from pathlib import Path

import networkx as nx

steps = 64
grid = Path("2023/inputs/day21_sm.txt").read_text().splitlines()

G = nx.Graph()

width = len(grid[0])
height = len(grid)
adjacents = [(0, 1), (0, -1), (1, 0), (-1, 0)]
edges = []
start = None
for y in range(height):
    for x in range(width):
        if grid[y][x] == "#":
            continue
        elif grid[y][x] == "S":
            start = (x, y)
        for o_x, o_y in adjacents:
            n_x = x + o_x
            n_y = y + o_y
            if 0 <= n_x < width and 0 <= n_y < height:
                if grid[n_y][n_x] != "#":
                    edges.append(((x, y), (n_x, n_y), 1))


visited = set()
queue = [start]
steps_available = steps
final_spots = set()
print("start", start)
while steps_available > 0:
    steps_available -= 1

    if steps_available == 0:
        final_spots.add((x, y))

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

print(len(queue))
