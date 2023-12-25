import itertools
from pathlib import Path


def parse_stone(stone):
    coords, velocity = stone.split(" @ ")
    x, y, z = tuple(map(int, coords.split(", ")))
    vx, vy, vz = tuple(map(int, velocity.split(", ")))
    return (x, y, z), (vx, vy, vz)


stones = list(map(parse_stone, Path("2023/inputs/day24.txt").read_text().splitlines()))

window_x1 = 200000000000000
window_x2 = 400000000000000
window_y1 = 200000000000000
window_y2 = 400000000000000

intersections = 0
for stone_a, stone_b in itertools.combinations(stones, 2):
    # check intersection
    m_a = stone_a[1][1] / stone_a[1][0]
    m_b = stone_b[1][1] / stone_b[1][0]

    # t = y - m*x
    t_a = stone_a[0][1] - m_a * stone_a[0][0]
    t_b = stone_b[0][1] - m_b * stone_b[0][0]

    if m_a == m_b:
        continue  # parallel

    intersection_x = (t_a - t_b) / (m_b - m_a)
    intersection_y = m_a * intersection_x + t_a

    if (
        window_x1 <= intersection_x <= window_x2
        and window_y1 <= intersection_y <= window_y2
        and (
            (intersection_x >= stone_a[0][0] and stone_a[1][0] > 0)
            or (intersection_x <= stone_a[0][0] and stone_a[1][0] <= 0)
        )
        and (
            (intersection_x >= stone_b[0][0] and stone_b[1][0] > 0)
            or (intersection_x <= stone_b[0][0] and stone_b[1][0] <= 0)
        )
    ):
        intersections += 1
print(intersections)
