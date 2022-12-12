import aocutils
from collections import defaultdict

grid = aocutils.read_lines("./2022/inputs/day12.txt")

pos_x = -1
pos_y = -1
target_x = -1
target_y = -1
height = len(grid)
width = len(grid[0])

a_positions = []
for y, row in enumerate(grid):
    grid[y] = list(row)
    for x, c in enumerate(row):
        if c == "S":
            pos_x = x
            pos_y = y
            grid[y][x] = ord("z")
            a_positions.append((x,y))
        elif c == "E":
            target_x = x
            target_y = y
            grid[y][x] = ord("z")
        else:
            if grid[y][x] == "a":
                a_positions.append((x,y))
            grid[y][x] = ord(grid[y][x])

i = 0
def dijkstra(sx, sy, tx, ty):
    global i
    q = set((x, y) for x in range(width) for y in range(height))
    dist = defaultdict(lambda: float("inf"))
    pre = defaultdict(lambda: None)
    dist[(sx,sy)] = 0
    while len(q) != 0:
        u = min(q, key=lambda x:dist[x])
        q.remove((u[0], u[1]))
        if u == (tx, ty):
            break 
        for nx, ny in [(u[0]+1, u[1]), (u[0]-1,u[1]), (u[0], u[1]+1), (u[0], u[1]-1)]:
            if (nx, ny) in q:
                new_dist = dist[u] + (1 if grid[ny][nx] - grid[u[1]][u[0]] <= 1 else float("inf"))
                if new_dist < dist[(nx, ny)]:
                    dist[(nx, ny)] = new_dist
                    pre[(nx, ny)] = u
    i += 1
    print("finshed", i)
    return dist[(tx,ty)]

def dijkstra2(sx, sy):
    global i
    q = set((x, y) for x in range(width) for y in range(height))
    dist = defaultdict(lambda: float("inf"))
    pre = defaultdict(lambda: None)
    dist[(sx,sy)] = 0
    while len(q) != 0:
        u = min(q, key=lambda x:dist[x])
        q.remove((u[0], u[1]))
        for nx, ny in [(u[0]+1, u[1]), (u[0]-1,u[1]), (u[0], u[1]+1), (u[0], u[1]-1)]:
            if (nx, ny) in q:
                new_dist = dist[u] + (1 if grid[u[1]][u[0]] - grid[ny][nx] <= 1 else float("inf"))
                if new_dist < dist[(nx, ny)]:
                    dist[(nx, ny)] = new_dist
                    pre[(nx, ny)] = u
    i += 1
    return dist


print(min([d for (x, y), d in dijkstra2(target_x, target_y).items() if (x,y) in a_positions]))
