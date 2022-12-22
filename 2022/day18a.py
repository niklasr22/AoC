import aocutils
import math

coords = aocutils.read_lines(
    "./2022/inputs/day18_test.txt", lambda c: tuple(map(int, c.split(",")))
)


def is_neighbour(coord1, coord2) -> bool:
    return math.sqrt(sum([(c1 - c2) ** 2 for c1, c2 in zip(coord1, coord2)])) == 1.0


surface = 0
for cube in coords:
    sides_free = 6
    for neighbour in coords:
        if cube != neighbour and is_neighbour(cube, neighbour):
            sides_free -= 1
    surface += sides_free

print(surface)
