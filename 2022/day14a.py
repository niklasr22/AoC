import aocutils
from collections import defaultdict

rocks = aocutils.read_lines("./2022/inputs/day14.txt")

cave = defaultdict(lambda: ".")
highest_y = 0
for r in rocks:
    positions = list(map(lambda p: list(map(int, p.split(","))), r.split(" -> ")))
    for i in range(1, len(positions)):
        x1 = min(positions[i - 1][0], positions[i][0])
        x2 = max(positions[i - 1][0], positions[i][0])
        y1 = min(positions[i - 1][1], positions[i][1])
        y2 = max(positions[i - 1][1], positions[i][1])
        highest_y = max(highest_y, y2)
        for y in range(y1, y2 + 1):
            for x in range(x1, x2 + 1):
                cave[(x, y)] = "#"


def drop_sand(ly) -> bool:
    sp = (500, 0)
    while sp[1] < ly:
        if cave[(sp[0], sp[1] + 1)] == ".":
            sp = sp[0], sp[1] + 1
        elif cave[(sp[0] - 1, sp[1] + 1)] == ".":
            sp = sp[0] - 1, sp[1] + 1
        elif cave[(sp[0] + 1, sp[1] + 1)] == ".":
            sp = sp[0] + 1, sp[1] + 1
        else:
            cave[sp] = "o"
            return True
    return False


i = 0
while drop_sand(highest_y):
    i += 1
print(i)
