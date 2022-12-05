import copy

data = open("./2020/day12/input.txt").read()
instructions = list(map(lambda row: [row[0], int(row[1:])], data.splitlines()))

we = 10
wn = 1

n = 0
e = 0


def rotate(r):
    global wn, we
    won = wn
    woe = we
    if r == 180 or r == -180:
        we *= -1
        wn *= -1
    elif r == 90 or r == -270:
        wn = -woe
        we = won
    elif r == -90 or r == 270:
        wn = woe
        we = -won


def adjustWaypoint(d, x):
    global wn, we
    if d == "N":
        wn += x
    elif d == "S":
        wn -= x
    elif d == "E":
        we += x
    elif d == "W":
        we -= x


def move(x):
    global n, e, we, wn
    n += wn * x
    e += we * x


for i in instructions:
    if i[0] == "R":
        dir = rotate(i[1])
    elif i[0] == "L":
        dir = rotate(-i[1])
    elif i[0] == "F":
        move(i[1])
    else:
        adjustWaypoint(i[0], i[1])
print(abs(n) + abs(e))
