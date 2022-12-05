from collections import defaultdict

data = open("./2021/day25/input.txt").read()
rows = data.splitlines()

grid = {
    (x, y): (1 if c == ">" else (2 if c == "v" else 0))
    for y, row in enumerate(rows)
    for x, c in enumerate(row)
}

MAX_Y = len(rows)
MAX_X = len(rows[0])


def move():
    global grid
    newGrid = defaultdict(lambda: 0)
    moved = False
    for (x, y), c in grid.items():
        if c == 1:
            newX = (x + 1) % MAX_X
            if (newX, y) not in grid or grid[(newX, y)] == 0:
                newGrid[(newX, y)] = c
                moved = True
            else:
                newGrid[(x, y)] = c
        elif c == 2:
            newGrid[(x, y)] = c
    grid = newGrid
    newGrid = defaultdict(lambda: 0)
    for (x, y), c in grid.items():
        if c == 2:
            newY = (y + 1) % MAX_Y
            if (x, newY) not in grid or grid[(x, newY)] == 0:
                newGrid[(x, newY)] = c
                moved = True
            else:
                newGrid[(x, y)] = c
        else:
            newGrid[(x, y)] = c
    grid = newGrid
    return moved


i = 1
while move():
    i += 1
print(i)
