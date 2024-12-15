from pathlib import Path

import numpy as np

data = Path("2024/inputs/day15.txt").read_text().strip()

map, movements = data.split("\n\n")


def expand_row(row):
    new_row = []
    for c in row:
        if c == "#":
            new_row.extend(["#", "#"])
        elif c == ".":
            new_row.extend([".", "."])
        elif c == "@":
            new_row.extend(["@", "."])
        elif c == "O":
            new_row.extend(["[", "]"])
    return new_row


map = np.array([expand_row(row) for row in map.splitlines()])

movements = list(movements.replace("\n", ""))

offsets = {
    "^": (-1, 0),
    "v": (1, 0),
    "<": (0, -1),
    ">": (0, 1),
}

pos = np.argwhere(map == "@")[0]


def push(target_pos, offset, dir, soft=False):
    value = map[*target_pos]
    if value == ".":
        return True
    if value == "#":
        return False
    if value == "[":
        next_pos = target_pos + offset
        possible = push(next_pos, offset, dir, soft=True)

        if dir in ["^", "v"]:
            possible = possible and push(next_pos + [0, 1], offset, dir, soft=True)

        if possible:
            push(next_pos, offset, dir, soft=soft)
            if dir in ["^", "v"]:
                push(next_pos + [0, 1], offset, dir, soft=soft)
                if not soft:
                    map[*(next_pos + [0, 1])] = "]"
                    map[*(target_pos + [0, 1])] = "."
            if not soft:
                map[*next_pos] = "["
                map[*target_pos] = "."
            return True
    if value == "]":
        next_pos = target_pos + offset
        possible = push(next_pos, offset, dir, soft=True)
        if dir in ["^", "v"]:
            possible = possible and push(next_pos - [0, 1], offset, dir, soft=True)
        if possible:
            push(next_pos, offset, dir, soft=soft)
            if dir in ["^", "v"]:
                push(next_pos - [0, 1], offset, dir, soft=soft)
                if not soft:
                    map[*(next_pos - [0, 1])] = "["
                    map[*(target_pos - [0, 1])] = "."
            if not soft:
                map[*next_pos] = "]"
                map[*target_pos] = "."
            return True

    return False


for step, dir in enumerate(movements):
    offset = offsets[dir]
    target_pos = pos + offset

    if push(target_pos, offset, dir):
        map[*pos] = "."
        pos = target_pos
        map[*target_pos] = "@"


boxes = np.argwhere(map == "[")
coords = 0
for box in boxes:
    coords += 100 * box[0] + box[1]

print(coords)
