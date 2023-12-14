from pathlib import Path

grid = list(map(list, Path("2023/inputs/day14.txt").read_text().splitlines()))

cols = [[grid[y][x] for y in range(len(grid))] for x in range(len(grid[0]))]


def find_weight(col: list[list]) -> int:
    try:
        first_still = col.index("#")
        stones = col[:first_still].count("O")
        return sum(range(len(col), len(col) - stones, -1)) + find_weight(
            col[first_still + 1 :]
        )
    except:
        return sum(range(len(col), len(col) - col.count("O"), -1))


print(sum(find_weight(col) for col in cols))
