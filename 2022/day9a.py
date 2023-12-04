from collections import namedtuple

import aocutils

moves = aocutils.read_lines("./2022/inputs/day9.txt")

s = [0, 0]

h_pos = [0, 0]
t_pos = [0, 0]

t_positions: set[tuple[int, int]] = set()
t_positions.add(tuple(t_pos))


def update_tail(dir):
    if (
        h_pos[0] - 1 <= t_pos[0] <= h_pos[0] + 1
        and h_pos[1] - 1 <= t_pos[1] <= h_pos[1] + 1
    ):
        return

    if abs(h_pos[1] - t_pos[1]) == 2:
        t_pos[0] = h_pos[0]
        if t_pos[1] < h_pos[1]:
            t_pos[1] = h_pos[1] - 1
        else:
            t_pos[1] = h_pos[1] + 1
    elif abs(h_pos[0] - t_pos[0]) == 2:
        t_pos[1] = h_pos[1]
        if t_pos[0] < h_pos[0]:
            t_pos[0] = h_pos[0] - 1
        else:
            t_pos[0] = h_pos[0] + 1


for move in moves:
    dir, steps = move.split(" ")
    steps = int(steps)
    for s in range(steps):
        match dir:
            case "U":
                h_pos[1] += 1
            case "D":
                h_pos[1] -= 1
            case "L":
                h_pos[0] -= 1
            case "R":
                h_pos[0] += 1
        update_tail(dir)
        t_positions.add(tuple(t_pos))

print(len(t_positions))
