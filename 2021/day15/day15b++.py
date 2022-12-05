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
    visited = set()
    heappush(heap, s)

    while heap:
        u = heappop(heap)
        if u[1] == t[0] and u[2] == t[1]:
            print(u[0])
            break
        for i in range(4):
            xx = u[1] + h[i]
            yy = u[2] + v[i]
            if (xx, yy) not in visited:
                if 0 <= xx < width * 5 and 0 <= yy < height * 5:
                    visited.add((xx, yy))
                    tx = xx // width
                    ty = yy // height
                    x = xx % width
                    y = yy % height
                    val = (int(rows[y][x]) + tx + ty - 1) % 9 + 1
                    heappush(heap, (u[0] + val, xx, yy))


dijkstra2((0, 0, 0), (width * 5 - 1, height * 5 - 1))
