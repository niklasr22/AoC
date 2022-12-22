import math
import sys

import aocutils

sys.setrecursionlimit(5000)

coords = aocutils.read_lines(
    "./2022/inputs/day18.txt", lambda c: tuple(map(int, c.split(",")))
)


def is_neighbour(coord1, coord2) -> bool:
    return math.sqrt(sum([(c1 - c2) ** 2 for c1, c2 in zip(coord1, coord2)])) == 1.0


def calc_surface(coords):
    surface = 0
    for cube in coords:
        sides_free = 6
        for neighbour in coords:
            if cube != neighbour and is_neighbour(cube, neighbour):
                sides_free -= 1
        surface += sides_free
    return surface


min_x = min_y = min_z = 0
max_x = max_y = max_z = 0

for x, y, z in coords:
    min_x = min(min_x, x)
    min_y = min(min_y, y)
    min_z = min(min_z, z)
    max_x = max(max_x, x)
    max_y = max(max_y, y)
    max_z = max(max_z, z)

air = set()
for x in range(min_x - 1, max_x + 2):
    for y in range(min_y - 1, max_y + 2):
        for z in range(min_z - 1, max_z + 2):
            coord = (x, y, z)
            if coord not in coords:
                air.add(coord)


def find_connected(cube, search_set: set, connected_cubes: set) -> set:
    if cube in search_set:
        search_set.remove(cube)
    neighbours = set(filter(lambda x: is_neighbour(cube, x), search_set))
    search_set.difference_update(neighbours)
    connected_cubes.add(cube)
    for n in neighbours:
        if n not in connected_cubes:
            find_connected(n, search_set.copy(), connected_cubes)


outer_air_shell = set()
find_connected((min_x - 1, min_y - 1, min_z - 1), air.copy(), outer_air_shell)

inner_air = air.difference(outer_air_shell)

naive_surface = calc_surface(coords)
surface = naive_surface - calc_surface(inner_air)

print(surface)
