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
            for offset_x, offset_y in environment:
                adjacent_x = x + offset_x
                adjacent_y = y + offset_y
                if 0 <= adjacent_y < h and 0 <= adjacent_x < w:
                    adjacent_char = schematic[adjacent_y][adjacent_x]
                    if (
                        adjacent_char.isascii()
                        and adjacent_char != "."
                        and not adjacent_char.isnumeric()
                    ):
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
