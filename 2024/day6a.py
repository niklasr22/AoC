from pathlib import Path

grid = Path("2024/inputs/day6.txt").read_text().strip().splitlines()

grid = (
    [["O"] * len(grid[0])]
    + [["O"] + list(row) + ["O"] for row in grid]
    + [["O"] * len(grid[0])]
)


dir = "up"
pos = (0, 0)

for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] == "^":
            pos = (y, x)
            break


offsets = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}


def timestep(pos, dir):
    oy, ox = offsets[dir]
    front = grid[pos[0] + oy][pos[1] + ox]
    if front == "O":
        # end
        return None, None
    elif front == "#":
        # turn right
        if dir == "up":
            dir = "right"
        elif dir == "right":
            dir = "down"
        elif dir == "down":
            dir = "left"
        elif dir == "left":
            dir = "up"
        return pos, dir
    return (pos[0] + oy, pos[1] + ox), dir


visited = set()
visited.add(pos)
while dir != None:
    pos, dir = timestep(pos, dir)
    if pos != None:
        visited.add(pos)

print(len(visited))
