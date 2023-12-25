import itertools
from functools import reduce
from pathlib import Path

import networkx as nx
import tqdm
from matplotlib import pyplot as plt

connections_list = Path("2023/inputs/day25.txt").read_text().splitlines()
edges = []
for conncector in connections_list:
    source, conns = conncector.split(": ")
    for neighbour in conns.split(" "):
        edges.append((source, neighbour))

G = nx.Graph()
G.add_edges_from(edges)

# for x in itertools.combinations(edges, 3):
#     G.remove_edges_from(x)
#     if nx.number_connected_components(G) > 1:
#         print(x)
#         print(
#             reduce(
#                 lambda a, b: a * b,
#                 [len(component) for component in nx.connected_components(G)],
#             )
#         )
#         exit()
#     G.add_edges_from(x)

# for x in tqdm.tqdm(itertools.combinations(edges, 2)):
#     G.remove_edges_from(x)

#     if nx.has_bridges(G):
#         bridges = list(nx.bridges(G))
#         G.remove_edges_from(bridges)
#         print(x)
#         print(
#             reduce(
#                 lambda a, b: a * b,
#                 [len(component) for component in nx.connected_components(G)],
#             )
#         )
#         exit()
#   G.add_edges_from(x)
nx.draw(
    G,
    with_labels=True,
)
plt.show()

# look for the 3 edges
G.remove_edges_from([("gpz", "prk"), ("zhg", "qdv"), ("lsk", "rfq")])

print(
    reduce(
        lambda a, b: a * b,
        [len(component) for component in nx.connected_components(G)],
    )
)
