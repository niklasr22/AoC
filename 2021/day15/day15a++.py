from collections import Counter
from collections import defaultdict
from heapq import heappop, heappush

data = open("./2021/day15/input.txt").read()
rows = data.splitlines()

h = [-1, 0, 1, 0]
v = [0, 1, 0, -1]

width = len(rows[0])
height = len(rows)


def dijkstra2(s, t):
    global width, height
    heap = []
    visited = []
    heappush(heap, s)

    while len(heap) > 0:
        u = heappop(heap)
        if u[1] == t[0] and u[2] == t[1]:
            print(u[0])
            break
        for i in range(4):
            xx = u[1] + h[i]
            yy = u[2] + v[i]
            if (xx, yy) not in visited:
                if 0 <= xx < width and 0 <= yy < height:
                    visited.append((xx, yy))
                    heappush(heap, (u[0] + int(rows[yy][xx]), xx, yy))


# print(walk(0,0,0),oalr)
print("started dijkstra")
dijkstra2((0, 0, 0), (width - 1, height - 1))
print("finished dijkstra")
