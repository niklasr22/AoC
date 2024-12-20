from collections import defaultdict
from heapq import heappop, heappush
from pathlib import Path

import numpy as np

data = Path("2024/inputs/day16.txt").read_text().strip()

grid = np.array([list(row) for row in data.splitlines()])

pos = np.argwhere(grid == "S")[0]
target = np.argwhere(grid == "E")[0]


offsets = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def neighbors(grid, pos):
    for rot, offset in enumerate(offsets):
        neighbor = tuple((np.array(pos) + offset).tolist())
        try:
            if grid[*neighbor] != "#":
                yield rot, neighbor
        except IndexError:
            pass


def dijkstra(grid, pos):
    prev = defaultdict(set)
    visited = {}
    q = [(0, (tuple(pos.tolist()), 0), None)]
    while q:
        dist, u, prev_u = heappop(q)

        if u in visited:
            if dist == visited[u]:
                prev[u].add(prev_u)
            continue

        if prev_u is not None:
            prev[u].add(prev_u)
        visited[u] = dist

        u_pos, u_dir = u
        for v_dir, v_pos in neighbors(grid, u_pos):
            key = (v_pos, v_dir)
            alt = dist + 1 + 1000 * (min(abs(v_dir - u_dir), 4 - abs(v_dir - u_dir)))
            if key in visited:
                continue
            heappush(q, (alt, key, u))
    return visited, prev


dists, prev = dijkstra(grid, pos)

for (pos, dir), cost in dists.items():
    if pos == tuple(target):
        print("A:", cost)
        break


def all_positions(x, prev, positions: set):
    for prev_x in prev[x]:
        positions.add(prev_x[0])
        all_positions(prev_x, prev, positions)
    return positions


x = (tuple(target.tolist()), dir)
viewing_positions = all_positions(x, prev, {x})
print("B:", len(viewing_positions))
