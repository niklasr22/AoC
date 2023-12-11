import itertools
from collections import defaultdict
from pathlib import Path

input_map: list[list] = list(
    map(list, Path("2023/inputs/day11.txt").read_text().splitlines())
)


galaxies = []
for y in range(len(input_map)):
    for x in range(len(input_map[0])):
        if input_map[y][x] == "#":
            galaxies.append((x, y))

# scale - 1 because the value is added
SCALE = 1000000 - 1
addition = 0
for y in range(len(input_map)):
    if not any(pos == "#" for pos in input_map[y]):
        for g in range(len(galaxies)):
            if galaxies[g][1] > y + addition:
                galaxies[g] = (galaxies[g][0], galaxies[g][1] + SCALE)
        addition += SCALE

addition = 0
for x in range(len(input_map[0])):
    if not any(input_map[y][x] == "#" for y in range(len(input_map))):
        for g in range(len(galaxies)):
            if galaxies[g][0] > x + addition:
                galaxies[g] = (galaxies[g][0] + SCALE, galaxies[g][1])
        addition += SCALE

distances = []
for combination in itertools.combinations(range(len(galaxies)), 2):
    pos1 = galaxies[combination[0]]
    pos2 = galaxies[combination[1]]

    # find dist
    dist = abs(pos2[1] - pos1[1]) + abs(pos2[0] - pos1[0])
    distances.append(dist)

print(sum(distances))
