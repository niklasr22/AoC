data = open("./2021/day5/input.txt").read()

rows = list(
    map(
        lambda y: list(map(lambda g: g.split(","), y.split(" -> "))),
        list(filter(lambda x: x != "", data.split("\n"))),
    )
)
# print(rows)

field = []
for i in range(2000):
    field.append([0] * 2000)

for p in rows:
    if p[0][0] == p[1][0]:
        y1 = min(int(p[0][1]), int(p[1][1]))
        y2 = max(int(p[0][1]), int(p[1][1]))
        for i in range(y1, y2 + 1):
            field[i][int(p[0][0])] += 1
    elif p[0][1] == p[1][1]:
        x1 = min(int(p[0][0]), int(p[1][0]))
        x2 = max(int(p[0][0]), int(p[1][0]))
        for i in range(x1, x2 + 1):
            field[int(p[1][1])][i] += 1
    else:
        x1 = min(int(p[0][0]), int(p[1][0]))
        x2 = max(int(p[0][0]), int(p[1][0]))
        y1 = min(int(p[0][1]), int(p[1][1]))
        y2 = max(int(p[0][1]), int(p[1][1]))
        y = 0
        d = 0
        x = 0
        dx = 0
        a = []
        b = []
        if int(p[0][0]) < int(p[1][0]):
            a = p[0]
            b = p[1]
        else:
            a = p[1]
            b = p[0]

        if int(a[0]) < int(b[0]):
            y = int(a[1])
            if int(a[1]) < int(b[1]):
                d = 1
            else:
                d = -1
        else:
            y = int(a[1])
            if int(a[1]) < int(b[1]):
                d = -1
            else:
                d = 1
        for i in range(int(a[0]), int(b[0]) + 1):
            field[y][i] += 1
            y += d

count = 0
for i in range(len(field)):
    for j in range(1000):
        if field[i][j] >= 2:
            count += 1

print(count)
