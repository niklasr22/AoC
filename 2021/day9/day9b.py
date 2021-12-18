data = open("./2021/day9/input.txt").read()
rows = list(map(lambda wort : [char for char in wort], data.splitlines()))

lowPoints = []
for y in range(len(rows)):
    for x in range(len(rows[y])):
        up = int(rows[y-1][x]) if y > 0 else 10
        down = int(rows[y+1][x]) if y < len(rows) - 1 else 10
        left = int(rows[y][x-1]) if x > 0 else 10
        right = int(rows[y][x+1]) if x < len(rows[y]) - 1 else 10

        pos = int(rows[y][x])
        if pos < up and pos < down and pos < left and pos < right:
            lowPoints.append((x,y))

def checkOtherForBasin(x, y, rows, basin):
    if y >= len(rows) or x >= len(rows[y]):
        return
    pos = int(rows[y][x]) if rows[y][x] != 'X' else 10
    if pos > 8:
        return
    basin.append((x,y))
    rows[y][x] = 'X'

    up = int(rows[y-1][x]) if y > 0 and rows[y-1][x] != 'X' else 10
    down = int(rows[y+1][x]) if y < len(rows) - 1 and rows[y+1][x] != 'X' else 10
    left = int(rows[y][x-1]) if x > 0 and rows[y][x-1] != 'X' else 10
    right = int(rows[y][x+1]) if x < len(rows[y]) - 1 and rows[y][x+1] != 'X' else 10

    if up < 10:
        checkOtherForBasin(x, y-1, rows, basin)
    if down < 10:
        checkOtherForBasin(x,y+1, rows, basin)
    if left < 10:
        checkOtherForBasin(x-1,y, rows, basin)
    if right < 10:
        checkOtherForBasin(x+1,y, rows, basin)
    
basinList = []
for x, y in lowPoints:
    basin = []
    checkOtherForBasin(x,y, rows, basin)
    basinList.append(basin)

#output field
#for i in rows:
#    print("".join(i))

basinList.sort(key=len, reverse=True)
count = 1
for i in range(3):
    count *= len(basinList[i])

print(count)