import sys
from pathlib import Path

import networkx as nx

sys.setrecursionlimit(1000000)
maze = Path("2023/inputs/day23.txt").read_text().splitlines()

neighbours = [(0, 1, "^"), (0, -1, "v"), (-1, 0, ">"), (1, 0, "<")]

height = len(maze)
width = len(maze[0])

edges = []
for y in range(height):
    for x in range(width):
        if maze[y][x] == "#":
            continue

        for o_x, o_y, _ in neighbours:
            n_x = x + o_x
            n_y = y + o_y
            if 0 <= n_x < width and 0 <= n_y < height:
                if maze[n_y][n_x] == "#":
                    continue
                edges.append(((x, y), (n_x, n_y), 1))


G = nx.Graph()
G.add_weighted_edges_from(edges)

# visualize graph
# PG = nx.nx_pydot.to_pydot(G)
# PG.write_png("day23_maze.png")

degrees = dict(G.degree())
seen = set()


def reduce_graph_dfs(node, previous):
    if degrees[node] != 2:
        seen.add(node)
        for neighbour in list(G.neighbors(node)):
            if neighbour in seen:
                continue
            if neighbour in G.nodes:
                reduce_graph_dfs(neighbour, node)
    else:
        weight1 = G.edges[previous, node]["weight"]
        G.remove_edge(previous, node)
        next = [n for n in list(G.neighbors(node)) if n != previous][0]
        weight2 = G.edges[node, next]["weight"]
        G.remove_edge(node, next)
        G.remove_node(node)
        G.add_edge(previous, next, weight=weight1 + weight2)

        reduce_graph_dfs(next, previous)


start = (maze[0].find("."), 0)
target = (maze[len(maze) - 1].find("."), len(maze) - 1)

reduce_graph_dfs(start, None)

# visualize reduced graph
# PG = nx.nx_pydot.to_pydot(G)
# PG.write_png("day23_maze_reduced.png")


longest_paths = nx.all_simple_paths(G, start, target)
print("Found all paths")

print(
    nx.path_weight(
        G, max(longest_paths, key=lambda p: nx.path_weight(G, p, "weight")), "weight"
    )
)
