data = open("./2021/day13/input.txt").read()
data = data.split("\n\n")
dots = list(map(lambda x: tuple(list(map(int, x.split(",")))), data[0].splitlines()))
folds = list(
    map(lambda x: x.replace("fold along ", "").split("="), data[1].splitlines())
)

dotsDict = dict()
for d in dots:
    dotsDict[d] = 0

for f in folds:
    newDots = dict()
    fl = int(f[1])
    if f[0] == "x":
        for d in dotsDict:
            if d[0] < fl:
                newDots[d] = 0
            else:
                newDots[(2 * fl - d[0], d[1])] = 0
    elif f[0] == "y":
        for d in dotsDict:
            if d[1] < fl:
                newDots[d] = 0
            else:
                newDots[(d[0], 2 * fl - d[1])] = 0
    dotsDict = newDots

maxX = 0
maxY = 0
for d in dotsDict.keys():
    maxX = d[0] if d[0] > maxX else maxX
    maxY = d[1] if d[1] > maxY else maxY

for y in range(maxY + 1):
    row = ""
    for x in range(maxX + 1):
        if (x, y) in dotsDict.keys():
            row += "#"
        else:
            row += " "
    print(row)
