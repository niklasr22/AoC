import aocutils

valley_map = aocutils.read_lines("./2022/inputs/day24.txt")

blizzards = []
blizzard_dir = []
for y, row in enumerate(valley_map):
    for x, c in enumerate(row):
        if c == "^":
            blizzards.append((x, y))
            blizzard_dir.append(0)
        elif c == "v":
            blizzards.append((x, y))
            blizzard_dir.append(2)
        elif c == ">":
            blizzards.append((x, y))
            blizzard_dir.append(1)
        elif c == "<":
            blizzards.append((x, y))
            blizzard_dir.append(3)

max_x = len(valley_map[0]) - 1
max_y = len(valley_map) - 1
width = max_x - 1
height = max_y - 1
start = (1, 0)
goal = (max_x - 1, max_y)

adjacents = [(0, -1), (1, 0), (0, 1), (-1, 0)]


def next_blizzards(blizzards, blizzard_dir) -> list:
    new_blizzards = []
    for (x, y), d in zip(blizzards, blizzard_dir):
        x = 1 + (x + adjacents[d][0] - 1) % width
        y = 1 + (y + adjacents[d][1] - 1) % height
        new_blizzards.append((x, y))
    return new_blizzards


def possible_neighbours(node, blizzards):
    positions = []
    for x, y in adjacents + [(0, 0)]:
        x += node[0]
        y += node[1]
        if (
            (x, y) == start
            or (x, y) == goal
            or (x > 0 and x < max_x and y > 0 and y < max_y)
        ):
            if (x, y) not in blizzards:
                positions.append((x, y))
    return positions


def bfs(start, goal, blizzard_dir):
    global blizzards
    blizzards_cache = {0: blizzards}
    seen = set()
    queue = []
    queue.append((start, 0))
    seen.add(start)
    while len(queue) != 0:
        node, min = queue.pop(0)
        if node == goal:
            return min

        if min not in blizzards_cache:
            blizzards = next_blizzards(blizzards_cache[min - 1], blizzard_dir)
            blizzards_cache[min] = blizzards
        else:
            blizzards = blizzards_cache[min]
        neighbours = possible_neighbours(node, blizzards)
        for child in neighbours:
            if (child, min + 1) not in seen:
                queue.append((child, min + 1))
                seen.add((child, min + 1))
    return -1


trip1 = bfs(start, goal, blizzard_dir) - 1
trip2 = bfs(goal, start, blizzard_dir)
trip3 = bfs(start, goal, blizzard_dir)

print(trip1, trip2, trip3, trip1 + trip2 + trip3)
