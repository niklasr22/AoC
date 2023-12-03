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

            for ox, oy in environment:
                ex = x + ox
                ey = y + oy
                if 0 <= ex < h and 0 <= ey < w:
                    e = schematic[ey][ex]
                    if e.isascii() and e != "." and not e.isnumeric():
                        is_adjacent = True
                        if e == "*":
                            adjacent_stars.add((ex, ey))
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
print(gear_candidates)
for gear, numbers in gear_candidates.items():
    if len(numbers) == 2:
        result += numbers[0] * numbers[1]

print(result)
