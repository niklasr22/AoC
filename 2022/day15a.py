import aocutils

readings = aocutils.read_lines("./2022/inputs/day15.txt")

sensors: dict[tuple[int,int], int] = {}
beacons: set[tuple[int, int]] = set()

for r in readings:
    splitted = r.split(",")
    sx = int(splitted[0].split("=")[1])
    sy = int(splitted[1].split(":")[0].split("=")[1])
    bx = int(splitted[1].split("=")[2])
    by = int(splitted[2].split("=")[1])

    sensors[(sx, sy)] = abs(sx - bx) + abs(sy - by)
    beacons.add((bx, by))

row_of_interest = 2000000

# sloooooooow
impossible_x: set[tuple[int, int]] = set()
for (sx, sy), d in sensors.items():
    imp_x_range_size = d - abs(sy - row_of_interest)
    if imp_x_range_size >= 0:
        for x in range(sx - imp_x_range_size, sx + imp_x_range_size + 1):
            if (x, row_of_interest) not in beacons:
                impossible_x.add((x, row_of_interest))

print(len(impossible_x))