from pathlib import Path

B = (0, 1)
T = (0, -1)
L = (-1, 0)
R = (1, 0)

dig_list = Path("2023/inputs/day18.txt").read_text().splitlines()

pos = (0, 0)
points = [pos]

real_pos = (0, 0)

for instruction in dig_list:
    dir, length, color = instruction.split(" ")
    length = int(length)
    pos = (pos[0], pos[1])
    points.append(pos)
    if dir == "R":
        points.append(pos)
        for i in range(length):
            npos = (pos[0] + 1 + i, pos[1])
            points.append(npos)
    elif dir == "L":
        points.append(pos)
        for i in range(length):
            npos = (pos[0] - 1 - i, pos[1])
            points.append(npos)
    elif dir == "U":
        points.append(pos)
        for i in range(length):
            npos = (pos[0], pos[1] - 1 - i)
            points.append(npos)
    elif dir == "D":
        for i in range(length):
            npos = (pos[0], pos[1] + 1 + i)
            points.append(npos)
    pos = npos


min_y = min([p[1] for p in points])
max_y = max([p[1] for p in points])

min_x = min([p[0] for p in points])
max_x = max([p[0] for p in points])


grid = set(points)

# mark outer ground tiles
adjacents = [B, T, L, R]
# +2 for border
height = abs(max_y - min_y) + 1 + 2
width = abs(max_x - min_x) + 1 + 2


# visualize lagoon
# for y in range(min_y - 1, max_y + 2):
#     row = ""
#     for x in range(min_x - 1, max_x + 2):
#         row += "#" if (x, y) in grid else "."
#     print(row)


search = [(min_x - 1, min_y - 1)]
visited = set()
while search:
    x, y = search.pop(0)

    if (x, y) in visited:
        continue

    visited.add((x, y))

    for o_x, o_y in adjacents:
        a_x = x + o_x
        a_y = y + o_y
        if min_x - 1 <= a_x <= max_x + 1 and min_y - 1 <= a_y <= max_y + 1:
            if (a_x, a_y) not in grid:
                search.append((a_x, a_y))

print(height * width - len(visited))


# for y in range(min_y - 1, max_y + 2):
#     row = ""
#     for x in range(min_x - 1, max_x + 2):
#         row += "#" if (x, y) in visited else "."
#     print(row)
