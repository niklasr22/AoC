import sys
from pathlib import Path

sys.setrecursionlimit(1000000)

maze = Path("2023/inputs/day23_sm.txt").read_text().splitlines()

neighbours = [(0, 1, "^"), (0, -1, "v"), (-1, 0, ">"), (1, 0, "<")]

height = len(maze)
width = len(maze[0])


def dfs(pos, target, seen: set):
    x, y = pos

    if pos == target:
        return 0

    new_path = 0

    new_seen = seen.copy()
    new_seen.add(pos)

    for o_x, o_y, blocker in neighbours:
        n_x = x + o_x
        n_y = y + o_y
        if 0 <= n_x < width and 0 <= n_y < height:
            if maze[n_y][n_x] in ["#", blocker]:
                continue
            if (n_x, n_y) not in seen:
                new_path = max(new_path, 1 + dfs((n_x, n_y), target, new_seen))

    return new_path


start = (maze[0].find("."), 0)
target = (maze[len(maze) - 1].find("."), len(maze) - 1)

print(dfs(start, target, set()))
