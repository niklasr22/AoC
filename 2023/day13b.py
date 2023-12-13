from pathlib import Path

patterns = list(
    map(str.splitlines, Path("2023/inputs/day13.txt").read_text().split("\n\n"))
)


def smudge_test(pattern1, pattern2):
    diffs = [0 if pattern1[i] == pattern2[i] else 1 for i in range(len(pattern1))]
    if sum(diffs) == 1:
        return True, diffs.index(1)
    return False, -1


def get_horizontal_reflection(pattern: list[str]):
    for y in range(1, len(pattern)):
        mirrors = True
        smudge = False
        for offset in range(1, min(y, len(pattern) - y) + 1):
            pattern1 = pattern[y - offset]
            pattern2 = pattern[y + offset - 1]
            if pattern1 != pattern2:
                smudge_loc, pos = smudge_test(pattern1, pattern2)
                if not smudge_loc:
                    mirrors = False
                    break
                else:
                    if smudge == True:
                        # too many smudges
                        mirrors = False
                        break
                    new_pattern2 = pattern2[:pos] + pattern1[pos] + pattern2[pos + 1 :]
                    new_pattern1 = pattern1[:pos] + pattern2[pos] + pattern1[pos + 1 :]
                    if pattern1 != new_pattern2 and new_pattern1 != pattern2:
                        mirrors = False
                        break
                    smudge = True
        if mirrors and smudge:
            return y
    return -1


def transpose(grid):
    transposed_grid = []
    for col in range(len(grid[0])):
        transposed_grid.append("".join([grid[y][col] for y in range(len(grid))]))
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
