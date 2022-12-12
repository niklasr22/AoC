from collections import defaultdict
import copy
from typing import Any, Callable


def read_file(filename: str) -> str:
    return open(filename).read()


def read_lines(
    filename: str,
    apply: Callable[[str], Any] | None = lambda x: x,
    ignore_empty_lines: bool = True,
) -> list:
    data = read_file(filename)
    return [
        apply(l)
        for l in data.splitlines()
        if not ignore_empty_lines or (ignore_empty_lines and l != "")
    ]


def read_blocks(
    filename: str,
    block_sep: str = "\n\n",
    apply_on_block: Callable[[str], Any] = lambda x: x,
) -> list:
    data = read_file(filename)
    return [apply_on_block(b.strip()) for b in data.split(block_sep) if b != ""]


def read_lineblocks(
    filename: str,
    block_sep: str = "\n\n",
    apply_on_line: Callable[[str], Any] | None = None,
) -> list:
    data = read_file(filename)
    return [
        [apply_on_line(l) for l in b.strip().split("\n") if l != ""]
        for b in data.split(block_sep)
        if b != ""
    ]

def flatten(list: list[list]) -> list:
    return [item for sublist in list for item in sublist]


def dijkstra(nodes: set, start, neighbour_func: callable, dist_func: callable, target=None) -> list:
    q = nodes.copy()
    dist = defaultdict(lambda: float("inf"))
    pre = defaultdict(lambda: None)
    dist[start] = 0
    while len(q) != 0:
        u = min(q, key=lambda x:dist[x])
        q.remove((u[0], u[1]))
        if target is not None and u == target:
            break 
        for n in neighbour_func(u):
            if n in q:
                new_dist = dist[u] + dist_func(u, n)
                if new_dist < dist[n]:
                    dist[n] = new_dist
                    pre[n] = u
    return dist