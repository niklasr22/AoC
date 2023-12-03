from collections import defaultdict
from pathlib import Path

schematic: list[str] = Path("2023/inputs/day3.txt").read_text().splitlines()


reading_num = False
num = ""
is_adjacent = False

environment = [(-1, 0), (1, 0), (-1, -1), (0, -1), (1, -1), (-1, 1), (0, 1), (1, 1)]

gear_candidates = defaultdict(list)

h = len(schematic)
w = len(schematic[0])
for y in range(h):
    adjacent_stars = set()
    for x in range(w):
        c = schematic[y][x]
        if c.isdigit():
            if not reading_num:
                reading_num = True
            num += c

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
                        if adjacent_char == "*":
                            adjacent_stars.add((adjacent_x, adjacent_y))
        if not c.isdigit() or x == w - 1:
            if reading_num:
                if is_adjacent:
                    for gear in adjacent_stars:
                        gear_candidates[gear].append(int(num))

                adjacent_stars.clear()
                num = ""
                is_adjacent = False
                reading_num = False


result = 0
for gear, numbers in gear_candidates.items():
    if len(numbers) == 2:
        result += numbers[0] * numbers[1]

print(result)
