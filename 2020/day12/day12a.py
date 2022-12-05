import copy

data = open("./2020/day12/input.txt").read()
instructions = list(map(lambda row: [row[0], int(row[1:])], data.splitlines()))

dir = "E"
n = 0
e = 0


def dirToRot(dir):
    if dir == "N":
        return 0
    elif dir == "S":
        return 180
    elif dir == "E":
        return 90
    elif dir == "W":
        return 270


def rotate(dir, r):
    r += dirToRot(dir)
    if r < 0:
        r = 360 + r
    r = r % 360
    if r == 90:
        return "E"
    elif r == 0:
        return "N"
    elif r == 180:
        return "S"
    elif r == 270:
        return "W"


def move(d, x):
    global n, e
    if d == "N":
        n += x
    elif d == "S":
        n -= x
    elif d == "E":
        e += x
    elif d == "W":
        e -= x


for i in instructions:
    if i[0] == "R":
        dir = rotate(dir, i[1])
    elif i[0] == "L":
        dir = rotate(dir, -i[1])
    elif i[0] == "F":
        move(dir, i[1])
    else:
        move(i[0], i[1])

print(abs(n) + abs(e))
