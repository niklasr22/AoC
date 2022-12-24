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


def do_move(steps, dir_x, dir_y, x, y) -> tuple[int, int]:
    for _ in range(steps):
        new_x = bounds_row[y][0] + (x + dir_x - bounds_row[y][0]) % bounds_row[y][2]
        new_y = bounds_col[x][0] + (y + dir_y - bounds_col[x][0]) % bounds_col[x][2]
        if raw_map[new_y][new_x] == "#":
            break
        x = new_x
        y = new_y
    return x, y


for steps, rot in zip(path_moves, path_turns):
    pos_x, pos_y = do_move(steps, move_x[facing], move_y[facing], pos_x, pos_y)

    if rot is not None:
        facing = (facing + (1 if rot == "R" else -1)) % 4

print(1000 * (pos_y + 1) + 4 * (pos_x + 1) + facing)
