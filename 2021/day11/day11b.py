data = open("./2021/day11/input2.txt").read()
rows = list(map(lambda x: list(map(int, [c for c in x])), data.splitlines()))

flashes = 0

h = [-1, -1, -1, 0, 0, 1, 1, 1]
v = [0, -1, 1, -1, 1, 0, -1, 1]

height = len(rows)
width = len(rows[0])


def updateAdjacent(x, y):
    global flashes
    for i in range(8):
        xx = x + h[i]
        yy = y + v[i]
        if 0 <= xx < height and 0 <= yy < width and rows[yy][xx] < 10:
            rows[yy][xx] += 1
            if rows[yy][xx] == 10:
                rows[yy][xx] += 1
                flashes += 1
                updateAdjacent(xx, yy)


s = 0
while True:
    for y in range(height):
        for x in range(width):
            if rows[y][x] < 10:
                rows[y][x] += 1
                if rows[y][x] == 10:
                    rows[y][x] += 1
                    flashes += 1
                    updateAdjacent(x, y)
    all = True
    for y in range(height):
        for x in range(width):
            if rows[y][x] >= 10:
                rows[y][x] = 0
            else:
                all = False
    if all:
        print(s)
        break
    s += 1
