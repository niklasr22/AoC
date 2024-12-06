from collections import defaultdict
from pathlib import Path

grid = Path("2024/inputs/day6.txt").read_text().strip().splitlines()

grid = (
    [["O"] * (len(grid[0]) + 2)]
    + [["O"] + list(row) + ["O"] for row in grid]
    + [["O"] * (len(grid[0]) + 2)]
)


dir = "up"
pos = (0, 0)

# find start
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


def rotate(dir):
    # turn right
    if dir == "up":
        dir = "right"
    elif dir == "right":
        dir = "down"
    elif dir == "down":
        dir = "left"
    elif dir == "left":
        dir = "up"
    return dir


def timestep(pos, dir):
    oy, ox = offsets[dir]
    front = grid[pos[0] + oy][pos[1] + ox]
    if front == "O":
        # end
        return None, None
    elif front == "#":
        # turn right
        return pos, rotate(dir)
    return (pos[0] + oy, pos[1] + ox), dir


orig_dir = dir
orig_pos = pos

loop_possibilities = set()
while dir != None:
    pos, dir = timestep(pos, dir)
    if pos != None:
        # check for loop when putting a wall in front
        oy, ox = offsets[dir]
        wall_candidate_pos = pos[0] + oy, pos[1] + ox

        if grid[wall_candidate_pos[0]][wall_candidate_pos[1]] == ".":
            # not already a wall
            test_dir = rotate(dir)

            test_visited = defaultdict(list)
            test_visited[orig_pos].append(orig_dir)
            grid[wall_candidate_pos[0]][wall_candidate_pos[1]] = "#"
            test_dir = orig_dir
            test_pos = orig_pos
            while test_dir != None:
                test_pos, test_dir = timestep(test_pos, test_dir)
                if test_dir != None:
                    # check for loop
                    if test_pos in test_visited and test_dir in test_visited[test_pos]:
                        loop_possibilities.add(wall_candidate_pos)
                        break
                    test_visited[test_pos].append(test_dir)

            # reset
            grid[wall_candidate_pos[0]][wall_candidate_pos[1]] = "."

print(len(loop_possibilities))
