import aocutils

rows = aocutils.read_lines("./2022/inputs/day8.txt")

visible_trees = []
for y in range(len(rows)):
    visible_trees.append([0] * len(rows[0]))

for y in range(len(rows)):
    highest = -1
    for x in range(len(rows[0])):
        tree = int(rows[y][x])
        if highest < tree:
            visible_trees[y][x] = 1
        highest = max(highest, tree)
    highest = -1
    for x in reversed(range(len(rows[0]))):
        tree = int(rows[y][x])
        if highest < tree:
            visible_trees[y][x] = 1
        highest = max(highest, tree)

for x in range(len(rows[0])):
    highest = -1
    for y in range(len(rows)):
        tree = int(rows[y][x])
        if highest < tree:
            visible_trees[y][x] = 1
        highest = max(highest, tree)
    highest = -1
    for y in reversed(range(len(rows))):
        tree = int(rows[y][x])
        if highest < tree:
            visible_trees[y][x] = 1
        highest = max(highest, tree)


print(sum(aocutils.flatten(visible_trees)))