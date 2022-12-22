import aocutils

rows = aocutils.read_lines("./2022/inputs/day8.txt")

visible_trees = []
for y in range(len(rows)):
    visible_trees.append([0] * len(rows[0]))


def get_viewing_dist(rows: list, tx: int, ty: int) -> int:
    if tx == 0 or ty == 0 or tx == len(rows[0]) - 1 or ty == len(rows) - 1:
        return 0
    height = rows[ty][tx]
    left = 0
    for x in reversed(range(tx)):
        left += 1
        if rows[ty][x] >= height:
            break
    right = 0
    for x in range(tx + 1, len(rows[0])):
        right += 1
        if rows[ty][x] >= height:
            break
    top = 0
    for y in reversed(range(ty)):
        top += 1
        if rows[y][tx] >= height:
            break
    bottom = 0
    for y in range(ty + 1, len(rows)):
        bottom += 1
        if rows[y][tx] >= height:
            break
    return left * right * top * bottom


rows = [[int(t) for t in row] for row in rows]
for y in range(len(rows)):
    for x in range(len(rows[0])):
        visible_trees[y][x] = get_viewing_dist(rows, x, y)

print(max(aocutils.flatten(visible_trees)))
