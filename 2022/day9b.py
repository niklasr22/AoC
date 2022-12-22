from collections import defaultdict
import aocutils

moves = aocutils.read_lines("./2022/inputs/day9.txt")


def printrope(rope):
    # JFF (and maybe for testing ;( )
    xs = [r[0] for r in rope] + [0]
    ys = [r[1] for r in rope] + [0]
    min_x = min(xs)
    max_x = max(xs)
    min_y = min(ys)
    max_y = max(ys)

    markers = defaultdict(lambda: ".")

    for i, r in enumerate(rope):
        if markers[tuple(r)] == ".":
            markers[tuple(r)] = str(i) if i != 0 else "H"

    if markers[(0, 0)] == ".":
        markers[(0, 0)] = "s"

    for y in reversed(range(min_y, max_y + 1)):
        print("".join(markers[(x, y)] for x in range(min_x, max_x + 1)))


rope = [[0, 0] for _ in range(10)]

t_positions: set[tuple[int, int]] = set()
t_positions.add(tuple(rope[-1]))


def update_tail(h, t):
    if (
        rope[h][0] - 1 <= rope[t][0] <= rope[h][0] + 1
        and rope[h][1] - 1 <= rope[t][1] <= rope[h][1] + 1
    ):
        return

    if rope[t][0] != rope[h][0]:
        rope[t][0] += 1 if rope[h][0] - rope[t][0] > 0 else -1
    if rope[t][1] != rope[h][1]:
        rope[t][1] += 1 if rope[h][1] - rope[t][1] > 0 else -1


for move in moves:
    dir, steps = move.split(" ")
    steps = int(steps)
    for s in range(steps):
        match dir:
            case "U":
                rope[0][1] += 1
            case "D":
                rope[0][1] -= 1
            case "L":
                rope[0][0] -= 1
            case "R":
                rope[0][0] += 1
        for tail in range(1, len(rope)):
            update_tail(tail - 1, tail)
        t_positions.add(tuple(rope[-1]))

# print(t_positions)
print(len(t_positions))
