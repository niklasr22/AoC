from pathlib import Path

import numpy as np

data = Path("2024/inputs/day15.txt").read_text().strip()

map, movements = data.split("\n\n")

map = np.array([list(row) for row in map.splitlines()])

movements = list(movements.replace("\n", ""))

offsets = {
    "^": (-1, 0),
    "v": (1, 0),
    "<": (0, -1),
    ">": (0, 1),
}

pos = np.argwhere(map == "@")[0]


def push(target_pos, offset):
    value = map[*target_pos]
    if value == ".":
        return True
    if value == "#":
        return False
    if value == "O":
        next_pos = target_pos + offset
        possible = push(next_pos, offset)
        if possible:
            map[*next_pos] = "O"
            map[*target_pos] = "."
            return True
    return False


for dir in movements:
    offset = offsets[dir]
    target_pos = pos + offset
    if push(target_pos, offset):
        map[*pos] = "."
        pos = target_pos
        map[*target_pos] = "@"

boxes = np.argwhere(map == "O")
coords = 0
for box in boxes:
    coords += box[0] * 100 + box[1]

print(coords)
