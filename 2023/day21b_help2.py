import math
from pathlib import Path

import networkx as nx

# (min_steps + 1)
steps = 50  # 14 * (9 // 2)
steps = 5  # 14 * 2 + 8 - 5

ms = 14
hb = (steps // ms) * 2 + 1

grid = Path("2023/inputs/day21_real_sq3x3.txt").read_text().splitlines()

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


G.add_weighted_edges_from(edges)
print(nx.dijkstra_path_length(G, start, target))

exit()


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

for y in range(height):
    row = ""

    if y % 11 == 0:
        print()
    for x in range(width):
        if x % 11 == 0:
            row += " "
        row += "O" if (x, y) in queue else ("." if grid[y][x] != "#" else "#")
    print(row)


def gauss(n):
    return n * (n + 1) / 2


def calc_cells(w):
    c = int(w**2 - 4 * gauss(math.ceil(w / 2) - 1))
    no_org_kind = 1 + sum(range(0, (c - 1) // 2 + 1 - 4, 8))
    return c, no_org_kind, c - no_org_kind


total_inner, no_org_kind_inner, no_other_kind_inner = calc_cells(hb)
print("HB", hb)
print(total_inner, no_org_kind_inner, no_other_kind_inner)

print(no_org_kind_inner * 39 + no_other_kind_inner * 42)
print(
    no_org_kind_inner * 42
    + no_other_kind_inner * 39
    + (17 + 15 + 18 + 15)
    + (6 + 9 + 2 + 9)
    + (6 + 36) * 3
    + (9 + 38) * 3
    + (2 + 29) * 3
    + (9 + 38) * 3
)
