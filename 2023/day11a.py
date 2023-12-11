import itertools
from collections import defaultdict
from pathlib import Path

input_map: list[list] = list(
    map(list, Path("2023/inputs/day11.txt").read_text().splitlines())
)


def transpose(grid):
    transposed_grid = []
    for col in range(len(grid[0])):
        transposed_grid.append([grid[y][col] for y in range(len(grid))])
    return transposed_grid


def duplicate_rows(grid: list[list]) -> list[list]:
    new_grid: list[list] = []
    for row in grid:
        try:
            row.index("#")
        except:
            new_grid.append(list(row))
        new_grid.append(list(row))
    return new_grid


galaxy_map = transpose(duplicate_rows(transpose(duplicate_rows(input_map))))

galaxies = []
for y in range(len(galaxy_map)):
    for x in range(len(galaxy_map[0])):
        if galaxy_map[y][x] == "#":
            galaxies.append((x, y))

distances = []
for combination in itertools.combinations(range(len(galaxies)), 2):
    pos1 = galaxies[combination[0]]
    pos2 = galaxies[combination[1]]

    # calculate distance
    distances.append(abs(pos2[1] - pos1[1]) + abs(pos2[0] - pos1[0]))

print(sum(distances))
