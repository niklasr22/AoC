from pathlib import Path

grid = Path("2023/inputs/day16.txt").read_text().splitlines()

# beam x, y, d (0,1,2,3) = (N,E,S,W)
beams = [(-1, 0, 1)]
energized = set()
seen = set()

dirs = {
    0: (0, -1),
    1: (1, 0),
    2: (0, 1),
    3: (-1, 0),
}

height = len(grid)
width = len(grid[0])

while beams:
    beam = beams.pop()
    if beam in seen:
        continue
    seen.add(beam)

    beam_x, beam_y, dir = beam

    next_pos_x = beam_x + dirs[dir][0]
    next_pos_y = beam_y + dirs[dir][1]

    if not (0 <= next_pos_x < width and 0 <= next_pos_y < height):
        # beam got outside
        continue

    energized.add((next_pos_x, next_pos_y))

    tile = grid[next_pos_y][next_pos_x]

    if (
        tile == "."
        or (tile == "-" and dir in [1, 3])
        or (tile == "|" and dir in [0, 2])
    ):
        beams.append((next_pos_x, next_pos_y, dir))
        continue
    elif tile == "|":
        beams.append((next_pos_x, next_pos_y, 0))
        beams.append((next_pos_x, next_pos_y, 2))
        continue
    elif tile == "-":
        beams.append((next_pos_x, next_pos_y, 3))
        beams.append((next_pos_x, next_pos_y, 1))
        continue
    elif tile == "/":
        if dir == 0:
            dir = 1
        elif dir == 1:
            dir = 0
        elif dir == 2:
            dir = 3
        elif dir == 3:
            dir = 2
    elif tile == "\\":
        if dir == 0:
            dir = 3
        elif dir == 1:
            dir = 2
        elif dir == 2:
            dir = 1
        elif dir == 3:
            dir = 0

    if not (0 <= next_pos_x < width and 0 <= next_pos_y < height):
        # beam got outside
        continue
    energized.add((next_pos_x, next_pos_y))
    beams.append((next_pos_x, next_pos_y, dir))

# print out grid
# for y in range(height):
#     line = ""
#     for x in range(width):
#         line += "." if (x, y) not in energized else "#"
#     print(line)

print(len(energized))
