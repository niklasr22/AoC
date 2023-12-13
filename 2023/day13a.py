from pathlib import Path

patterns = list(
    map(str.splitlines, Path("2023/inputs/day13.txt").read_text().split("\n\n"))
)


def get_vertical_reflection(pattern: list[str]):
    ...


def get_horizontal_reflection(pattern: list[str]):
    for y in range(1, len(pattern)):
        mirrors = True
        for offset in range(1, min(y, len(pattern) - y) + 1):
            if pattern[y - offset] != pattern[y + offset - 1]:
                mirrors = False
                break
        if mirrors:
            return y
    return -1


def transpose(grid):
    transposed_grid = []
    for col in range(len(grid[0])):
        transposed_grid.append([grid[y][col] for y in range(len(grid))])
    return transposed_grid


result = 0
for pattern in patterns:
    vert = get_horizontal_reflection(transpose(pattern))
    if vert != -1:
        result += vert
        continue

    horizontal = get_horizontal_reflection(pattern)
    if horizontal != -1:
        result += horizontal * 100

print(result)
