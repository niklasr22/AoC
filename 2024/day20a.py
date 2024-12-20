import sys
from collections import Counter, defaultdict
from functools import cache
from heapq import heappop, heappush
from pathlib import Path

import numpy as np

data = Path("2024/inputs/day20.txt").read_text().strip()

grid = np.array([list(row) for row in data.splitlines()])

pos = np.argwhere(grid == "S")[0]
target = np.argwhere(grid == "E")[0]


offsets = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def neighbors(grid, pos, cheats_left):
    for offset in offsets:
        neighbor = tuple((np.array(pos) + offset).tolist())
        try:
            if (
                neighbor[0] >= 0
                and neighbor[1] >= 0
                and neighbor[0] < grid.shape[0]
                and neighbor[1] < grid.shape[1]
            ):
                if cheats_left > 0:
                    yield grid[*neighbor] == "#", neighbor
                elif grid[*neighbor] != "#":
                    yield False, neighbor
        except IndexError:
            pass


def dijkstra(grid, pos, cheats=0):
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

        u_pos, u_cheat = u
        for v_cheat, v_pos in neighbors(grid, u_pos, cheats - u_cheat):

            key = (v_pos, u_cheat + v_cheat)
            alt = dist + 1
            if key in visited:
                continue
            heappush(q, (alt, key, u))
    return visited, prev


c = Counter()


# @cache
# def dfs(pos, dist, default_dist, cheats_left):
#     if grid[*pos] == "E":
#         if dist < default_dist:
#             c[default_dist - dist] += 1
#             if default_dist - dist >= 100:
#                 return 1
#         return 0

#     ways = 0
#     for neighbor in neighbors(grid, pos, cheats_left):
#         if neighbor in seen:
#             continue
#         seen.add(neighbor)

#         # print(neighbor, grid[*neighbor[1]], cheats_left, cheats_left - neighbor[0])
#         if dfs(neighbor[1], dist + 1, default_dist, cheats_left - neighbor[0]):
#             ways += 1
#         seen.remove(neighbor)
#     return ways


dists, prev = dijkstra(grid, pos)

no_cheat_dist = dists[(tuple(target), 0)]
print("A:", no_cheat_dist)

stones = np.argwhere(grid == "#")
for i, stone in enumerate(stones):
    if (
        stone[0] == 0
        or stone[1] == 0
        or stone[0] == grid.shape[0] - 1
        or stone[1] == grid.shape[1] - 1
    ):
        continue
    grid[*stone] = "."
    dists, prev = dijkstra(grid, pos)
    d = dists[(tuple(target), 0)]
    if d < no_cheat_dist:
        c[no_cheat_dist - d] += 1
    grid[*stone] = "#"
    print(i, "/", len(stones))

print(c)

print(sum(v for k, v in c.items() if k >= 100))

# seen = {tuple(pos.tolist())}
# possibilities = dfs(tuple(pos.tolist()), 0, no_cheat_dist, 1)

# print("Two cheats:", possibilities)
# print(c)
