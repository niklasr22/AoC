import aocutils

# from interval import interval as iv

readings = aocutils.read_lines("./2022/inputs/day15.txt")

sensors: dict[tuple[int, int], int] = {}
beacons: set[tuple[int, int]] = set()

for r in readings:
    splitted = r.split(",")
    sx = int(splitted[0].split("=")[1])
    sy = int(splitted[1].split(":")[0].split("=")[1])
    bx = int(splitted[1].split("=")[2])
    by = int(splitted[2].split("=")[1])

    sensors[(sx, sy)] = abs(sx - bx) + abs(sy - by)
    # print((sx, sy), sensors[(sx, sy)])
    beacons.add((bx, by))

MAX_COORD_VAL = 4000000
# MAX_COORD_VAL = 20


"""
# suuuuuuuuuper slow
def get_imp_x_for_y(row_of_interest) -> iv:
    x_imp_iv = iv()
    for (sx, sy), d in sensors.items():
        imp_x_range_size = d - abs(sy - row_of_interest)
        if imp_x_range_size >= 0:
            x_imp_iv = x_imp_iv | iv((max(sx - imp_x_range_size, 0), min(MAX_COORD_VAL, sx + imp_x_range_size)))

    return x_imp_iv

for y in range(0, MAX_COORD_VAL + 1):
    impx = get_imp_x_for_y(y)
    if len(impx) > 1:
        for f,n in zip(impx[:-1], impx[1:]):
            if int(n[0]) - int(f[1]) > 1:
                signal = (int(f[1]) + 1) * 4000000 + y
                print(f[1], y, signal)
                exit(0)"""


# pretty fast B)
def points_to_lin(x1, y1, m) -> int:
    return y1 - m * x1


asc_lines = []
desc_lines = []
for (sx, sy), d in sensors.items():
    # add lines outside of sensor range
    asc_lines.append((sx - d - 1, sy, sx, sy + d + 1, points_to_lin(sx - d - 1, sy, 1)))
    asc_lines.append((sx, sy - d - 1, sx + d + 1, sy, points_to_lin(sx, sy - d - 1, 1)))
    desc_lines.append(
        (sx - d - 1, sy, sx, sy - d - 1, points_to_lin(sx - d - 1, sy, -1))
    )
    desc_lines.append(
        (sx, sy + d + 1, sx + d + 1, sy, points_to_lin(sx, sy + d + 1, -1))
    )

candidates = set()
for al in asc_lines:
    for dl in desc_lines:
        intersection_x = (dl[4] - al[4]) / 2
        intersection_y = intersection_x + al[4]
        isec = (intersection_x, intersection_y)
        if (
            dl[0] <= intersection_x <= dl[2]
            and 0 <= intersection_x <= MAX_COORD_VAL
            and 0 <= intersection_y <= MAX_COORD_VAL
        ):
            candidates.add(isec)

not_candidates = set()
for cx, cy in candidates:
    for (sx, sy), d in sensors.items():
        if abs(sx - cx) + abs(sy - cy) <= d:
            not_candidates.add((cx, cy))
candidates.difference_update(not_candidates)
for cx, cy in candidates:
    print(cx * 4000000 + cy)
