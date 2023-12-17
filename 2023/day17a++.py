from collections import defaultdict
from heapq import heappop, heappush
from pathlib import Path


def get_neighbours(x, y):
    return [(x + 1, y, 1), (x - 1, y, 3), (x, y + 1, 2), (x, y - 1, 0)]


def bfs(grid: list[list[int]], target=None) -> defaultdict:
    queue = []
    dist = defaultdict(lambda: float("inf"))

    # queue item struct: heatloss, (x,y), dir, dir_duration
    start_south = (0, (0, 0), 1, 1)
    start_east = (0, (0, 0), 2, 1)

    heappush(queue, start_east)
    heappush(queue, start_south)

    seen = set()

    while queue:
        (heatloss, (x, y), dir, dir_duration) = heappop(queue)

        dist[(x, y)] = heatloss

        if target is not None and (x, y) == target:
            break

        node = ((x, y), dir, dir_duration)
        if node in seen:
            continue

        seen.add(node)

        for nx, ny, nd in get_neighbours(x, y):
            if not (0 <= nx < len(grid[0]) and 0 <= ny < len(grid)):
                continue
            ndd = dir_duration + 1 if nd == dir else 1
            if ndd > 3:
                continue
            if (nd - 2) % 4 == dir:
                continue
            heappush(
                queue,
                (
                    heatloss + grid[ny][nx],
                    (nx, ny),
                    nd,
                    dir_duration + 1 if nd == dir else 1,
                ),
            )
    return dist


grid = [
    list(map(int, list(line)))
    for line in Path("2023/inputs/day17.txt").read_text().splitlines()
]

target = (len(grid[0]) - 1, len(grid) - 1)

results = bfs(grid, target)
print(results[target])
