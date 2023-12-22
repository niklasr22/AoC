import math
from pathlib import Path

import networkx as nx


def grid_copy(grid, copies):
    new_grid = []

    for y_c in range(copies):
        for y in range(len(grid)):
            new_grid.append(grid[y] * copies)

    grid_txt = "\n".join(new_grid)
    grid_txt = grid_txt.replace("S", ".", (copies * copies) // 2)
    grid_txt = grid_txt[: grid_txt.find("S") + 1] + grid_txt[
        grid_txt.find("S") + 1 :
    ].replace("S", ".")

    return grid_txt.splitlines()


ms = 130
steps = 2 * ms + 85
# steps = 1 + 20 + 10 + 8
# steps = 1 + 131 + 26501365 % 131 + 26501365 % ms
# steps = 1 + 20 + 10 + 2
# 1 + shortest path between starting points of two grid copies * 2 (because of alternating state) + steps % previous + steps % ms

hb = (steps // ms) * 2 - 1

grid_orig = Path("2023/inputs/day21.txt").read_text().splitlines()

orig_width = len(grid_orig[0])
orig_height = len(grid_orig)

grid = grid_copy(grid_orig, 5)


width = len(grid[0])
height = len(grid)

adjacents = [(0, 1), (0, -1), (1, 0), (-1, 0)]

start = None
for y in range(height):
    for x in range(width):
        if grid[y][x] == "S":
            start = (x, y)

queue = [start]
steps_available = steps
while steps_available > 0:
    steps_available -= 1

    new_queue = set()
    for x, y in queue:
        for o_x, o_y in adjacents:
            n_x = x + o_x
            n_y = y + o_y
            if 0 <= n_x < width and 0 <= n_y < height:
                if grid[n_y][n_x] != "#":
                    new_queue.add((n_x, n_y))
    starting_points = queue
    queue = new_queue

print(len(queue))

for y in range(height):
    row = ""

    if y % orig_height == 0:
        print()
    for x in range(width):
        if x % orig_width == 0:
            row += " "
        row += "O" if (x, y) in queue else ("." if grid[y][x] != "#" else "#")
    print(row)

print(hb, steps)
exit()

sub_grids = []
print(sub_grids)

sep_grid_row = None
for y in range(height):
    row = ""
    if y % orig_height == 0:
        if sep_grid_row:
            sub_grids.append(sep_grid_row)
        sep_grid_row = [["" for _ in range(orig_height)] for _ in range(7)]
        print()
    for x in range(width):
        if x % orig_width == 0:
            # print(x // orig_width)
            row += " "
        sep_grid_row[x // orig_width][y % orig_height] += (
            "O" if (x, y) in queue else ("." if grid[y][x] != "#" else "#")
        )
        row += "O" if (x, y) in queue else ("." if grid[y][x] != "#" else "#")
    print(row)
sub_grids.append(sep_grid_row)

print("-----------------------")
# print("\n".join(sub_grids[-1][3]))

print("Top", "\n".join(sub_grids[0][3]).count("O"))
print("Bottom", "\n".join(sub_grids[-1][3]).count("O"))
print("Left", "\n".join(sub_grids[3][0]).count("O"))
print("Right", "\n".join(sub_grids[3][-1]).count("O"))


print("OTL", "\n".join(sub_grids[2][0]).count("O"))
print("OTLI", "\n".join(sub_grids[2][1]).count("O"))
print("OBL", "\n".join(sub_grids[4][0]).count("O"))
print("OBLI", "\n".join(sub_grids[4][1]).count("O"))

print("OTR", "\n".join(sub_grids[2][-1]).count("O"))
print("OTRI", "\n".join(sub_grids[2][-2]).count("O"))
print("OBR", "\n".join(sub_grids[4][-1]).count("O"))
print("OBRI", "\n".join(sub_grids[4][-2]).count("O"))

print("CENTER", "\n".join(sub_grids[3][3]).count("O"))
print("ALTERNATE", "\n".join(sub_grids[3][2]).count("O"))
