from functools import cache
from pathlib import Path

input_grid = list(map(list, Path("2023/inputs/day14.txt").read_text().splitlines()))

# transform grid to a list of columns instead of a list of rows
transformed_grid = tuple(
    tuple(input_grid[y][x] for y in range(len(input_grid)))
    for x in range(len(input_grid[0]))
)


def find_weight(col: tuple[str]) -> int:
    return sum(len(col) - y for y in range(len(col)) if col[y] == "O")


@cache
def tilt(col: tuple[str]):
    try:
        first_solid_stone = col.index("#")
        stones = col[:first_solid_stone].count("O")
        remaining_col = tilt(col[first_solid_stone + 1 :])
        return (
            ("O",) * stones
            + (".",) * (first_solid_stone - stones)
            + ("#",)
            + remaining_col
        )
    except ValueError:
        stones = col.count("O")
        return ("O",) * stones + (".",) * (len(col) - stones)


def rotate_grid(grid: tuple[tuple[str]]):
    """
    Rotates a grid by 90 degrees clockwise
    """
    return tuple(
        tuple(grid[x][y] for x in range(len(grid)))
        for y in range(len(grid[0]) - 1, -1, -1)
    )


def perform_spin_cycle(grid: tuple[tuple[str]]):
    for _ in range(4):
        new_grid = list()
        for col in grid:
            new_col = tilt(col)
            new_grid.append(new_col)
        grid = rotate_grid(new_grid)
    return grid


grids = [transformed_grid]
cycles = 0
while True:
    grid = perform_spin_cycle(grids[-1])
    if grid in grids:
        break
    grids.append(grid)
    cycles += 1

loop_start = grids.index(grid)
loop_length = cycles - loop_start + 1

print("Detected a loop at", cycles, "spin cycles; loop length:", loop_length)
final_grid = grids[loop_start + (1000000000 - loop_start) % loop_length]

weight = sum(find_weight(col) for col in final_grid)
print("Weight:", weight)
