from collections import Counter, defaultdict
from heapq import heappop, heappush
from pathlib import Path

import numpy as np

OFFSETS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

data = Path("2024/inputs/day20.txt").read_text().strip()

grid = np.array([list(row) for row in data.splitlines()])


def neighbors(grid, pos, cheat_allowed):
    for offset in OFFSETS:
        neighbor = tuple((np.array(pos) + offset).tolist())
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


def dijkstra(grid, pos, cheats=False, cutoff=None):
    prev = {}
    visited = {}
    q = [(0, tuple(pos.tolist()))]
    while q:
        dist, u_pos = heappop(q)

        if u_pos in visited:
            continue

        visited[u_pos] = dist

        if cutoff is not None and dist >= cutoff:
            continue

        for _, v_pos in neighbors(grid, u_pos, cheats):
            alt = dist + 1
            key = v_pos

            if key not in visited or alt < visited[key]:
                heappush(q, (alt, key))
                prev[v_pos] = u_pos
    return visited, prev


def get_path_iter(pos, prev, path: list):
    while pos is not None:
        path.append(pos)
        pos = prev.get(pos)
    return list(reversed(path))


def get_cheat_possibilities(grid, cheat_length):
    origin = np.argwhere(grid == "S")[0]
    target = np.argwhere(grid == "E")[0]

    no_cheat_dists, prev = dijkstra(grid, origin)

    path = get_path_iter(tuple(target.tolist()), prev, [])

    c = Counter()
    for i, spos in enumerate(path):
        sdists, prev = dijkstra(
            grid,
            np.array(spos),
            cheats=True,
            cutoff=cheat_length,
        )
        dist_to_spos = no_cheat_dists[spos]

        for (pos), dist in sdists.items():
            if grid[*pos] == "#" or pos == spos:
                continue

            cheat_dist = dist_to_spos + dist
            normal_dist = no_cheat_dists[pos]

            saving = normal_dist - cheat_dist

            if saving >= 100:
                c[saving] += 1
    return sum(c.values())


print("A:", get_cheat_possibilities(grid, 2))
print("B:", get_cheat_possibilities(grid, 20))
