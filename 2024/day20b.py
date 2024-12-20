import sys
from collections import Counter, defaultdict
from heapq import heappop, heappush
from pathlib import Path

import numpy as np

sys.setrecursionlimit(10**9)
print(sys.getrecursionlimit())

data = Path("2024/test/day20.txt").read_text().strip()

grid = np.array([list(row) for row in data.splitlines()])

pos = np.argwhere(grid == "S")[0]
target = np.argwhere(grid == "E")[0]


offsets = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def neighbors(grid, pos, cheat_allowed):
    for offset in offsets:
        neighbor = tuple((np.array(pos) + offset).tolist())
        try:
            if (
                neighbor[0] >= 0
                and neighbor[1] >= 0
                and neighbor[0] < grid.shape[0]
                and neighbor[1] < grid.shape[1]
            ):
                if cheat_allowed:
                    yield grid[*neighbor] == "#", neighbor
                elif grid[*neighbor] != "#":
                    yield False, neighbor
        except IndexError:
            pass


def dijkstra(grid, pos, cheats=False):
    prev = defaultdict(set)
    visited = {}
    q = [(0, -1, (tuple(pos.tolist()), (None, None)), None)]
    ecount = 0
    while q:
        dist, _, u, prev_u = heappop(q)

        if u in visited:
            if dist <= visited[u]:
                prev[u].add(prev_u)
            continue

        if prev_u is not None:
            prev[u].add(prev_u)
        visited[u] = dist

        u_pos, (u_cheat, cheat_start) = u
        for v_cheat, v_pos in neighbors(
            grid, u_pos, cheats and (u_cheat is None or dist - cheat_start < 20)
        ):
            alt = dist + 1
            cheat = (None, None)
            if cheats:
                if v_cheat and u_cheat is None:
                    cheat = (v_pos, alt)
                elif u_cheat is not None:
                    cheat = (u_cheat, cheat_start)

            key = (v_pos, cheat)
            if key in visited:
                continue
            heappush(q, (alt, ecount, key, u))
            ecount += 1
    return visited, prev


c = Counter()

# def dfs(pos, dist, default_dist, cheats_left, cheat_duration=-1):
#     if grid[*pos] == "E":
#         if dist < default_dist:
#             c[default_dist - dist] += 1
#             if default_dist - dist >= 100:
#                 return 1
#         return 0

#     ways = 0
#     for cheating, neighbor in neighbors(grid, pos, cheats_left or cheat_duration > 0):
#         if neighbor in seen:
#             continue
#         seen.add(neighbor)

#         if cheating:
#             cd = 20
#             cl = False
#         else:
#             cl = cheats_left
#             cd = cheat_duration

#         if cheating and cl:
#             print("wtf")

#         if cd > 0:
#             cd -= 1

#         # if cd > 0:
#         #     print(cd, cheating, cheats_left, grid[*neighbor], cd, cl)
#         if dfs(neighbor, dist + 1, default_dist, cl, cd):
#             ways += 1
#         seen.remove(neighbor)
#     return ways


dists, _ = dijkstra(grid, pos)

no_cheat_dist = dists[(tuple(target), (None, None))]
print("A:", no_cheat_dist)


def all_positions(x, prev, positions: set, c):
    for prev_x in prev[x]:
        positions.add(prev_x[0])
        all_positions(prev_x, prev, positions)
    return positions


def get_no_paths(x, prev):
    if not prev[x]:
        return 1
    return sum(get_no_paths(p, prev) for p in prev[x])


def get_no_cheats(x, prev, cheats, dist):
    if not prev[x]:
        return 1
    pos, cheat = x
    if dist[(pos, cheat)] - cheat[1] == 20 or (
        dist[(pos, cheat)] - cheat[1] < 20 and pos == tuple(target.tolist())
    ):
        cheats.add((pos, cheat))

    for pos, cheat in prev[x]:
        if cheat == (None, None):
            continue
        # if dist[(pos, cheat)] - dist[(cheat[0], (None, None))] == 20:
        get_no_cheats((pos, cheat), prev, cheats, dist)


dists, prev = dijkstra(grid, pos, True)

c = Counter()

for (pos, cheat), dist in dists.items():
    if pos == tuple(target.tolist()) and no_cheat_dist - dist >= 50:
        print(cheat)
        cheats = set()
        get_no_cheats((pos, cheat), prev, cheats, dists)
        c[no_cheat_dist - dist] += len(cheats)
        # c[no_cheat_dist - dist] += get_no_paths((pos, cheat), prev)

print(c)
