from collections import defaultdict
from pathlib import Path

import numpy as np

data = Path("2024/test/day16.txt").read_text().strip()

grid = np.array([list(row) for row in data.splitlines()])

pos = np.argwhere(grid == "S")[0]
target = np.argwhere(grid == "E")[0]


def init_dist(grid, pos, prev):
    dist = dict()

    for y in range(grid.shape[0]):
        for x in range(grid.shape[1]):
            for d in range(4):
                dist[((y, x), d)] = float("inf")

    prev = defaultdict(lambda: None)
    for dir in range(4):
        dist[(tuple(pos.tolist()), dir)] = 0
    return dist, prev


offsets = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def neighbors(grid, pos, dir):
    for offset, ndir in [
        (offsets[dir], dir),
        ((0, 0), (dir - 1) % 4),
        ((0, 0), (dir + 1) % 4),
    ]:
        try:
            if grid[*(np.array(pos) + offset)] != "#":
                yield ndir, tuple((np.array(pos) + offset).tolist())
        except IndexError:
            pass


def dijkstra(grid, pos, target):
    dir = 0
    dist, prev = init_dist(grid, pos, target)
    q = set(dist.keys())
    while q:
        u = min(q, key=dist.get)
        q.remove(u)
        dir = u[1]
        for n_dir, v_pos in neighbors(grid, u[0], dir):
            if v_pos == u[0]:
                alt = dist[u] + 1000
            else:
                alt = dist[u] + 1
            key = (tuple(v_pos), n_dir)
            if alt < dist[key]:
                dist[key] = alt
                prev[key] = u
    return dist, prev


dists, prev = dijkstra(grid, pos, target)

for (pos, dir), cost in dists.items():
    if pos == tuple(target):
        print(cost)
        break
