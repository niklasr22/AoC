data = open("./2020/day17/input.txt").read()
rows = data.splitlines()

grid = dict()
z = 0
x = 0
y = 0
for r in rows:
    x = 0
    for c in r:
        grid[(x, y, z)] =  1 if c == '#' else 0
        x += 1
    y += 1

def updateCube(grid, newGrid, p, inGrid = True):
    if p in newGrid:
        return
    activeNeighbours = 0
    x = p[0]
    y = p[1]
    z = p[2]
    v = grid[p] if p in grid else 0
    for zz in range(z - 1, z + 2):
        for xx in range(x - 1, x + 2):
            for yy in range(y - 1, y + 2):
                if p == (xx, yy, zz):
                    continue
                if (xx, yy, zz) in grid:
                    activeNeighbours += grid[(xx, yy, zz)]
                elif inGrid:
                    updateCube(grid, newGrid, (xx, yy, zz), False)
    #if inGrid:
        #print(p, activeNeighbours)
    if v == 0 and activeNeighbours == 3:
        newGrid[p] = 1
    elif v == 1 and (activeNeighbours == 2 or activeNeighbours == 3):
        newGrid[p] = 1
    else:
        newGrid[p] = 0

for step in range(6):
    newGrid = dict()
    for p,v in grid.items():
        updateCube(grid, newGrid, p)
    grid = newGrid

print(sum(grid.values()))