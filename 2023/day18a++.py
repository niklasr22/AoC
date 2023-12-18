from pathlib import Path

from shapely import Polygon

dig_list = Path("2023/inputs/day18.txt").read_text().splitlines()

pos = (0, 0)
points = [pos]

cell_side_ref = {
    "H": 0,  # 0 = left, 1 = right
    "V": 0,  # 0 = top, 1 = bottom
}

dir_map = {
    0: "R",
    2: "L",
    1: "D",
    3: "U",
}


def parse_instruction(instruction):
    dir, length, _ = instruction.split(" ")
    return int(length), dir


for i, instruction in enumerate(dig_list):
    length, dir = parse_instruction(instruction)
    _, next_dir = parse_instruction(dig_list[(i + 1) % len(dig_list)])

    if dir == "R":
        addition = 0
        if cell_side_ref["H"] == 0 and next_dir != "U":
            addition = 1
            cell_side_ref["H"] = 1
        elif cell_side_ref["H"] == 1 and next_dir == "U":
            addition = -1
            cell_side_ref["H"] = 0

        npos = (pos[0] + length + addition, pos[1])
        points.append(npos)
    elif dir == "L":
        addition = 0
        if cell_side_ref["H"] == 1 and next_dir != "D":
            addition = 1
            cell_side_ref["H"] = 0
        elif cell_side_ref["H"] == 0 and next_dir == "D":
            addition = -1
            cell_side_ref["H"] = 1
        npos = (pos[0] - length - addition, pos[1])
        points.append(npos)
    elif dir == "U":
        addition = 0
        if cell_side_ref["V"] == 1 and next_dir != "L":
            addition = 1
            cell_side_ref["V"] = 0
        elif cell_side_ref["V"] == 0 and next_dir == "L":
            addition = -1
            cell_side_ref["V"] = 1
        npos = (pos[0], pos[1] - length - addition)
        points.append(npos)
    elif dir == "D":
        addition = 0
        if cell_side_ref["V"] == 0 and next_dir != "R":
            addition = 1
            cell_side_ref["V"] = 1
        elif cell_side_ref["V"] == 1 and next_dir == "R":
            addition = -1
            cell_side_ref["V"] = 0
        npos = (pos[0], pos[1] + length + addition)
        points.append(npos)
    pos = npos

polygon = Polygon(points)
print(int(polygon.area))
