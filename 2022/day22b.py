import re

import aocutils

lines = aocutils.read_lines("./2022/inputs/day22.txt", ignore_empty_lines=False)

raw_map = lines[: lines.index("")]
raw_path = lines[lines.index("") + 1]
path_moves = list(map(int, re.findall("[\d]+", raw_path)))
path_turns = re.findall("[RL]", raw_path) + [None]

bounds_row = dict()
for y, row in enumerate(raw_map):
    start_x = min(row.find("."), row.find("#") if "#" in row else 99999)
    start_y = max(row.rfind("."), row.rfind("#")) + 1

    bounds_row[y] = (start_x, start_y, start_y - start_x)


wrap_map = {}


def rrange(start: int, stop: int):
    return reversed(range(start, stop))


def map_vertical_to_horizontal(
    x_1: int, y_1: any, x_2: any, y_2: int, f1: int, f2: int
):
    for y_src, x_dest in zip(y_1, x_2):
        wrap_map[(x_1, y_src)] = (x_dest, y_2, f1)
        wrap_map[(x_dest, y_2)] = (x_1, y_src, f2)


def map_vertical_to_vertical(x_1: int, y_1: any, x_2: int, y_2: any, f1: int, f2: int):
    for y_src, y_dest in zip(y_1, y_2):
        wrap_map[(x_1, y_src)] = (x_2, y_dest, f1)
        wrap_map[(x_2, y_dest)] = (x_1, y_src, f2)


def map_horizontal_to_vertical(
    x_1: any, y_1: int, x_2: int, y_2: any, f1: int, f2: int
):
    for x_src, y_dest in zip(x_1, y_2):
        wrap_map[(x_src, y_1)] = (x_2, y_dest, f1)
        wrap_map[(x_2, y_dest)] = (x_src, y_1, f2)


def map_horizontal_to_horizontal(
    x_1: any, y_1: int, x_2: any, y_2: int, f1: int, f2: int
):
    for x_src, x_dest in zip(x_1, x_2):
        wrap_map[(x_src, y_1)] = (x_dest, y_2, f1)
        wrap_map[(x_dest, y_2)] = (x_src, y_1, f2)


"""
# test
map_horizontal_to_horizontal(range(8, 12), -1, rrange(0, 4), 3, 1, 1)  # orange
map_horizontal_to_vertical(range(4, 8), 3, 7, range(0, 4), 0, 1)  # red
map_vertical_to_horizontal(-1, range(4, 8), rrange(12, 16), 12, 3, 0)  # pink
map_horizontal_to_horizontal(range(0, 4), 8, rrange(8, 12), 12, 3, 3)  # yellow
map_horizontal_to_vertical(range(4, 8), 8, 7, rrange(8, 12), 0, 3)  # dark green
map_vertical_to_vertical(12, range(0, 4), 16, rrange(8, 12), 2, 2)  # blue
map_vertical_to_horizontal(12, range(4, 8), rrange(12, 16), 7, 1, 2)  # light green
"""

map_horizontal_to_horizontal(range(100, 150), -1, range(0, 50), 200, 3, 1)  # red
map_horizontal_to_vertical(range(50, 100), -1, -1, range(150, 200), 0, 1)  # purple
map_horizontal_to_vertical(range(0, 50), 99, 49, range(50, 100), 0, 1)  # yellow
map_vertical_to_vertical(49, range(0, 50), -1, rrange(100, 150), 0, 0)  # pink
map_vertical_to_horizontal(100, range(50, 100), range(100, 150), 50, 3, 2)  # blue
map_vertical_to_vertical(150, range(0, 50), 100, rrange(100, 150), 2, 2)  # green
map_vertical_to_horizontal(50, range(150, 200), range(50, 100), 150, 3, 2)  # orange

max_x = max(len(r) for r in raw_map)
bounds_col = dict()
for x in range(max_x):
    start_y = -1
    end_y = -1
    for y, row in enumerate(raw_map):
        if len(row) <= x:
            if start_y != -1 and end_y == -1:
                end_y = y
                break
        elif row[x] != " ":
            if start_y == -1:
                start_y = y
        elif row[x] == " " and start_y != -1:
            end_y = y
            break
    if end_y == -1:
        end_y = y + 1
    bounds_col[x] = (start_y, end_y, end_y - start_y)

pos_x = raw_map[0].find(".")
pos_y = 0
facing = 0  # > 0; v 1; < 2; ^ 3
move_x = {0: 1, 1: 0, 2: -1, 3: 0}
move_y = {0: 0, 1: 1, 2: 0, 3: -1}


def do_move(steps, dir_x, dir_y, x, y, facing) -> tuple[int, int]:
    for _ in range(steps):
        new_x = x + dir_x
        new_y = y + dir_y
        new_facing = facing
        if (new_x, new_y) in wrap_map:
            new_x, new_y, new_facing = wrap_map[(new_x, new_y)]
            dir_x = move_x[new_facing]
            dir_y = move_y[new_facing]
            new_x += dir_x
            new_y += dir_y
        if raw_map[new_y][new_x] == "#":
            break
        x = new_x
        y = new_y
        facing = new_facing
    return x, y, facing


for steps, rot in zip(path_moves, path_turns):
    pos_x, pos_y, facing = do_move(
        steps, move_x[facing], move_y[facing], pos_x, pos_y, facing
    )

    if rot is not None:
        facing = (facing + (1 if rot == "R" else -1)) % 4

print(1000 * (pos_y + 1) + 4 * (pos_x + 1) + facing)
