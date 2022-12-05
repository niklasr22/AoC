data = open("./2021/day13/input.txt").read()
data = data.split("\n\n")
dots = list(map(lambda x: tuple(list(map(int, x.split(",")))), data[0].splitlines()))
folds = list(
    map(lambda x: x.replace("fold along ", "").split("="), data[1].splitlines())
)

dotsDict = dict()
for d in dots:
    dotsDict[d] = 0

f = folds[0]
newDots = dict()
if f[0] == "x":
    x = int(f[1])
    for d in dotsDict:
        if d[0] < x:
            newDots[d] = 0
        else:
            newX = x - (d[0] - x)
            newDots[(newX, d[1])] = 0
elif f[0] == "y":
    y = int(f[1])
    for d in dotsDict:
        if d[1] < y:
            newDots[d] = 0
        else:
            newY = y - (d[1] - y)
            newDots[(d[0], newY)] = 0
print(len(newDots))
