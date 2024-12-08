from collections import defaultdict
from itertools import combinations
from pathlib import Path

import numpy as np

data = Path("2024/inputs/day8.txt").read_text().strip()

grid = np.array([list(row) for row in data.splitlines()])
width = len(grid[0])
height = len(grid)

unique_antenna_types = set(list(data)).difference({".", "\n"})


def get_anti_nodes(b: bool) -> int:
    anti_nodes = set()
    for antenna_type in unique_antenna_types:
        positions = np.argwhere(grid == antenna_type)
        for pair in combinations(positions, 2):
            orig_dist = pair[1] - pair[0]
            dist = orig_dist.copy()
            inside = True

            while inside:
                an1 = pair[0] - dist
                an2 = pair[1] + dist
                inside = False
                if 0 <= an1[0] < height and 0 <= an1[1] < width:
                    anti_nodes.add(tuple(an1))
                    inside = True
                if 0 <= an2[0] < height and 0 <= an2[1] < width:
                    anti_nodes.add(tuple(an2))
                    inside = True
                dist += orig_dist

                inside = inside and b

            if b:
                anti_nodes.add(tuple(pair[0]))
                anti_nodes.add(tuple(pair[1]))
    return len(anti_nodes)


print("A:", get_anti_nodes(False))
print("B:", get_anti_nodes(True))
