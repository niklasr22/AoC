data = open("./2021/day9/input.txt").read()
rows = list(map(lambda wort: [int(char) for char in wort], data.splitlines()))

h = [0, 1, 0, -1]
v = [1, 0, -1, 0]

riskLevel = 0
height = len(rows)
width = len(rows[0])
lowPoints = []
for y in range(height):
    for x in range(width):
        lower = True
        pos = rows[y][x]
        for i in range(4):
            nx = x + h[i]
            ny = y + v[i]
            if 0 <= nx < width and 0 <= ny < height and pos >= rows[ny][nx]:
                lower = False
        if lower:
            riskLevel += 1 + pos
            lowPoints.append((x, y))

print("a", riskLevel)


def checkOtherForBasin(x, y, rows, basin):
    pos = rows[y][x]
    if pos > 8:
        return basin
    rows[y][x] = 10
    for i in range(4):
        nx = x + h[i]
        ny = y + v[i]
        if 0 <= nx < width and 0 <= ny < height:
            basin = checkOtherForBasin(nx, ny, rows, basin)
    return basin + 1


basinList = []
for x, y in lowPoints:
    basin = checkOtherForBasin(x, y, rows, 0)
    basinList.append(basin)
basinList.sort(reverse=True)
count = 1
for i in basinList[:3]:
    count *= i
print("b", count)
