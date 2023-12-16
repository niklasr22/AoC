from pathlib import Path

grid = Path("2023/inputs/day16.txt").read_text().splitlines()


dirs = {
    0: (0, -1),
    1: (1, 0),
    2: (0, 1),
    3: (-1, 0),
}

height = len(grid)
width = len(grid[0])


def get_energized(start_x, start_y, start_dir):
    # beam x, y, d (0,1,2,3) = (N,E,S,W)
    beams = [(start_x, start_y, start_dir)]
    energized = set()
    seen = set()

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

    return len(energized)


energized_tiles = []
for y in range(height):
    energized_tiles.append(get_energized(-1, y, 1))
    energized_tiles.append(get_energized(width, y, 3))

for x in range(width):
    energized_tiles.append(get_energized(x, -1, 2))
    energized_tiles.append(get_energized(x, height, 0))

print(max(energized_tiles))
