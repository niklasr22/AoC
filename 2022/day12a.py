import aocutils
from collections import defaultdict

grid = aocutils.read_lines("./2022/inputs/day12.txt")

pos_x = -1
pos_y = -1
target_x = -1
target_y = -1
height = len(grid)
width = len(grid[0])

for y, row in enumerate(grid):
    grid[y] = list(row)
    for x, c in enumerate(row):
        if c == "S":
            pos_x = x
            pos_y = y
            grid[y][x] = ord("z")
        elif c == "E":
            target_x = x
            target_y = y
            grid[y][x] = ord("z")
        else:
            grid[y][x] = ord(grid[y][x])

def dijkstra(sx, sy, tx, ty):
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
    print(dist[(tx,ty)])

dijkstra(pos_x, pos_y, target_x, target_y)
