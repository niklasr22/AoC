from collections import defaultdict
from pathlib import Path

sketch = Path("2023/inputs/day10.txt").read_text().splitlines()

B = (0, 1)
T = (0, -1)
L = (-1, 0)
R = (1, 0)


def find_s(sketch: list[str]):
    for y, row in enumerate(sketch):
        x = row.find("S")
        if x != -1:
            break
    width = len(sketch[0])
    height = len(sketch)
    bottom = (
        sketch[y + B[1]][x + B[0]]
        if 0 <= x + B[0] < width and 0 <= y + B[1] < height
        else "."
    )
    top = (
        sketch[y + T[1]][x + T[0]]
        if 0 <= x + T[0] < width and 0 <= y + T[1] < height
        else "."
    )
    left = (
        sketch[y + L[1]][x + L[0]]
        if 0 <= x + L[0] < width and 0 <= y + L[1] < height
        else "."
    )
    right = (
        sketch[y + R[1]][x + R[0]]
        if 0 <= x + R[0] < width and 0 <= y + R[1] < height
        else "."
    )

    if bottom in ["|", "L", "J"]:
        if top in ["|", "F", "7"]:
            return "|", x, y
        elif right in ["-", "J", "7"]:
            return "F", x, y
        elif left in ["-", "L", "F"]:
            return "7", x, y
    elif top in ["|", "F", "7"]:
        if right in ["-", "J", "7"]:
            return "L", x, y
        elif left in ["-", "L", "F"]:
            return "J", x, y
    elif right in ["-", "J", "7"] and left in ["-", "L", "F"]:
        return "-", x, y
    return "E", -1, -1


def create_grid(sketch, sx, sy):
    grid = defaultdict(list)
    x, y = sx, sy

    search = [(x, y)]

    while search:
        x, y = search.pop(0)
        if (x, y) in grid:
            continue

        pipe = sketch[y][x]
        if pipe == "J":
            grid[(x, y)].append((x + L[0], y + L[1]))
            grid[(x, y)].append((x + T[0], y + T[1]))
            search.append((x + L[0], y + L[1]))
            search.append((x + T[0], y + T[1]))
        elif pipe == "|":
            grid[(x, y)].append((x + B[0], y + B[1]))
            grid[(x, y)].append((x + T[0], y + T[1]))
            search.append((x + B[0], y + B[1]))
            search.append((x + T[0], y + T[1]))
        elif pipe == "-":
            grid[(x, y)].append((x + L[0], y + L[1]))
            grid[(x, y)].append((x + R[0], y + R[1]))
            search.append((x + L[0], y + L[1]))
            search.append((x + R[0], y + R[1]))
        elif pipe == "L":
            grid[(x, y)].append((x + T[0], y + T[1]))
            grid[(x, y)].append((x + R[0], y + R[1]))
            search.append((x + T[0], y + T[1]))
            search.append((x + R[0], y + R[1]))
        elif pipe == "F":
            grid[(x, y)].append((x + B[0], y + B[1]))
            grid[(x, y)].append((x + R[0], y + R[1]))
            search.append((x + B[0], y + B[1]))
            search.append((x + R[0], y + R[1]))
        elif pipe == "7":
            grid[(x, y)].append((x + B[0], y + B[1]))
            grid[(x, y)].append((x + L[0], y + L[1]))
            search.append((x + B[0], y + B[1]))
            search.append((x + L[0], y + L[1]))
    return grid


s, sx, sy = find_s(sketch)
if s == "E":
    exit(-1)

sketch[sy] = sketch[sy].replace("S", s)
grid = create_grid(sketch, sx, sy)

sketch_just_loop = []
for row in sketch:
    sketch_just_loop.append(list(row))

for y in range(len(sketch_just_loop)):
    for x in range(len(sketch_just_loop[0])):
        if (x, y) not in grid:
            sketch_just_loop[y][x] = "."

upscaled_sketch = []
for y in range(len(sketch_just_loop)):
    upscaled_sketch.extend([[], [], []])
    for x in range(len(sketch_just_loop[0])):
        if sketch_just_loop[y][x] == ".":
            upscaled_sketch[y * 3] += "..."
            upscaled_sketch[y * 3 + 1] += "..."
            upscaled_sketch[y * 3 + 2] += "..."
        if sketch_just_loop[y][x] == "-":
            upscaled_sketch[y * 3] += "..."
            upscaled_sketch[y * 3 + 1] += "---"
            upscaled_sketch[y * 3 + 2] += "..."
        if sketch_just_loop[y][x] == "|":
            upscaled_sketch[y * 3] += ".|."
            upscaled_sketch[y * 3 + 1] += ".|."
            upscaled_sketch[y * 3 + 2] += ".|."
        if sketch_just_loop[y][x] == "L":
            upscaled_sketch[y * 3] += ".|."
            upscaled_sketch[y * 3 + 1] += ".L-"
            upscaled_sketch[y * 3 + 2] += "..."
        if sketch_just_loop[y][x] == "F":
            upscaled_sketch[y * 3] += "..."
            upscaled_sketch[y * 3 + 1] += ".F-"
            upscaled_sketch[y * 3 + 2] += ".|."
        if sketch_just_loop[y][x] == "J":
            upscaled_sketch[y * 3] += ".|."
            upscaled_sketch[y * 3 + 1] += "-J."
            upscaled_sketch[y * 3 + 2] += "..."
        if sketch_just_loop[y][x] == "7":
            upscaled_sketch[y * 3] += "..."
            upscaled_sketch[y * 3 + 1] += "-7."
            upscaled_sketch[y * 3 + 2] += ".|."

# mark outer ground tiles
adjacents = [B, T, L, R]
height = len(upscaled_sketch)
width = len(upscaled_sketch[0])
search = [(0, 0)]
while search:
    x, y = search.pop(0)
    if upscaled_sketch[y][x] == "O":
        continue
    for o_x, o_y in adjacents:
        a_x = x + o_x
        a_y = y + o_y
        if 0 <= a_x < width and 0 <= a_y < height:
            a_char = upscaled_sketch[a_y][a_x]
            if a_char == ".":
                upscaled_sketch[a_y][a_x] == "O"
                search.append((a_x, a_y))
    upscaled_sketch[y][x] = "O"

# downscale sketch
downscaled_sketch = []
for y in range(1, height, 3):
    downscaled_sketch.append([])
    for x in range(1, width, 3):
        downscaled_sketch[-1] += upscaled_sketch[y][x]


downscaled_sketch_str = "\n".join("".join(row) for row in downscaled_sketch)
print(downscaled_sketch_str.count("."))
