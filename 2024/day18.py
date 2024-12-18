import re
from collections import defaultdict
from heapq import heappop, heappush
from pathlib import Path

import numpy as np

OFFSETS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

data = np.array(
    list(
        map(int, re.findall(r"\d+", Path("2024/inputs/day18.txt").read_text().strip()))
    )
).reshape(-1, 2)

width = height = 70
pos = (0, 0)
target = (width, height)


def neighbors(pos, blocked):
    for offset in OFFSETS:
        neighbor = tuple((np.array(pos) + offset).tolist())
        try:
            if (
                neighbor not in blocked
                and neighbor[0] >= 0
                and neighbor[1] >= 0
                and neighbor[0] <= width
                and neighbor[1] <= height
            ):
                yield neighbor
        except IndexError:
            pass


def dijkstra(pos, blocked):
    visited = {}
    q = [(0, pos)]
    while q:
        dist, u = heappop(q)

        if u in visited:
            continue

        visited[u] = dist

        u_pos = u

        for v_pos in neighbors(u_pos, blocked):
            alt = dist + 1
            if v_pos in visited:
                continue
            heappush(q, (alt, v_pos))
    return visited


fallen = set(map(tuple, data[:1024].tolist()))
for stone_count, byte in enumerate(data[1024:]):
    fallen.add(tuple(byte.tolist()))

    distances = dijkstra(pos, fallen)

    if stone_count == 0:
        print("A:", distances[target])

    if target not in distances:
        print(f"B: {byte[0]},{byte[1]}")
        break
