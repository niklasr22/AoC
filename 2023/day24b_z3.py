from pathlib import Path

import z3


def parse_stone(stone):
    coords, velocity = stone.split(" @ ")
    x, y, z = tuple(map(int, coords.split(", ")))
    vx, vy, vz = tuple(map(int, velocity.split(", ")))
    return (x, y, z), (vx, vy, vz)


stones = list(map(parse_stone, Path("2023/inputs/day24.txt").read_text().splitlines()))

throw_pos = z3.RealVector("P", 3)
throw_vel = z3.RealVector("V", 3)
t = z3.RealVector("T", 3)
s = z3.Solver()

for i, stone in enumerate(stones[:3]):
    s.add(
        throw_pos[0] + t[i] * throw_vel[0] == stone[0][0] + t[i] * stone[1][0],
        throw_pos[1] + t[i] * throw_vel[1] == stone[0][1] + t[i] * stone[1][1],
        throw_pos[2] + t[i] * throw_vel[2] == stone[0][2] + t[i] * stone[1][2],
    )
s.check()
print(s.model().eval(sum(throw_pos)))
