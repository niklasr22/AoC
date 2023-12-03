from pathlib import Path

schematic: list[str] = Path("2023/inputs/day3.txt").read_text().splitlines()


result = 0
reading_num = False
num = ""
is_adjacent = False

environment = [(-1, 0), (1, 0), (-1, -1), (0, -1), (1, -1), (-1, 1), (0, 1), (1, 1)]

h = len(schematic)
w = len(schematic[0])
for y in range(h):
    for x in range(w):
        c = schematic[y][x]
        if c.isdigit():
            if not reading_num:
                reading_num = True
            num += c

            # check env
            for ox, oy in environment:
                ex = x + ox
                ey = y + oy
                if 0 <= ex < h and 0 <= ey < w:
                    e = schematic[ey][ex]
                    if e.isascii() and e != "." and not e.isnumeric():
                        is_adjacent = True
                        break
        else:
            if reading_num:
                if is_adjacent:
                    result += int(num)
                num = ""
                is_adjacent = False
                reading_num = False

print(result)
