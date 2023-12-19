from collections import defaultdict
from pathlib import Path

grid = Path("2023/inputs/day17.txt").read_text().splitlines()


hop_range = range(4, 11)

nodes = [
    (x, y, d, hops)
    for x in range(len(grid[0]))
    for y in range(len(grid))
    for hops in hop_range
    for d in range(4)
]
dirs = {
    0: (0, -1),
    1: (1, 0),
    2: (0, 1),
    3: (-1, 0),
}

edges = defaultdict(list)
edges_costs = dict()
for y in range(len(grid)):
    for x in range(len(grid[0])):
        for in_dir in range(4):
            for in_hops in hop_range:
                for out_dir in range(4):
                    for out_hops in hop_range:
                        out_dir_xy = dirs[out_dir]
                        n_x, n_y = (
                            x + out_dir_xy[0] * out_hops,
                            y + out_dir_xy[1] * out_hops,
                        )
                        if not (0 <= n_x < len(grid[0]) and 0 <= n_y < len(grid)):
                            continue

                        if in_dir != out_dir and (out_dir - 2) % 4 != in_dir:
                            edges[(x, y, in_dir, in_hops)].append(
                                (n_x, n_y, out_dir, out_hops)
                            )
                            edges_costs[
                                ((x, y, in_dir, in_hops), (n_x, n_y, out_dir, out_hops))
                            ] = (
                                sum(
                                    int(grid[y][dx])
                                    for dx in range(min(x, n_x), max(x, n_x) + 1)
                                )
                                - int(grid[y][x])
                                if out_dir in [1, 3]
                                else sum(
                                    int(grid[dy][x])
                                    for dy in range(min(y, n_y), max(y, n_y) + 1)
                                )
                                - int(grid[y][x])
                            )


# edges to target
tx = len(grid[0]) - 1
ty = len(grid) - 1

nodes.append((0, 0, -1, -1))  # start
nodes.append((tx, ty, -1, -1))  # target

for in_dir in range(4):
    for in_hops in hop_range:
        edges[(tx, ty, in_dir, in_hops)].append((tx, ty, -1, -1))
        edges_costs[((tx, ty, in_dir, in_hops), (tx, ty, -1, -1))] = 0


for out_dir in range(4):
    for out_hops in hop_range:
        edges[(0, 0, -1, -1)].append((0, 0, out_dir, out_hops))
        edges_costs[((0, 0, -1, -1), (0, 0, out_dir, out_hops))] = 0

print("Built graph", len(nodes))

import networkx as nx

G = nx.DiGraph()
e = [(a, b, cost) for (a, b), cost in edges_costs.items()]
G.add_weighted_edges_from(e)

start = (0, 0, -1, -1)
target = (tx, ty, -1, -1)

print(nx.dijkstra_path_length(G, start, target))
