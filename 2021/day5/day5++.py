from collections import defaultdict

data = open("./2021/day5/input.txt").read()
rows = list(
    map(
        lambda y: list(map(lambda g: list(map(int, g.split(","))), y.split(" -> "))),
        list(filter(lambda x: x != "", data.split("\n"))),
    )
)
grid = defaultdict(lambda: 0)
for p in rows:
    if p[0][0] == p[1][0]:
        for i in range(min(p[0][1], p[1][1]), max(p[0][1], p[1][1]) + 1):
            grid[(p[0][0], i)] += 1
    elif p[0][1] == p[1][1]:
        for i in range(min(p[0][0], p[1][0]), max(p[0][0], p[1][0]) + 1):
            grid[(i, p[1][1])] += 1
    else:  # b
        dx = 1
        dy = 1
        if p[0][0] > p[1][0]:
            dx = -1
        if p[0][1] > p[1][1]:
            dy = -1
        for x, y in zip(
            range(p[0][0], p[1][0] + dx, dx), range(p[0][1], p[1][1] + dy, dy)
        ):
            grid[(x, y)] += 1
count = 0
for i in grid.values():
    if i > 1:
        count += 1
print(count)
