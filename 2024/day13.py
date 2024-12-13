import re
from pathlib import Path

import numpy as np

machines = np.array(
    list(
        map(int, re.findall(r"\d+", Path("2024/inputs/day13.txt").read_text().strip()))
    )
).reshape(-1, 6)


def cost(machine, part2=False) -> int:
    a = np.array([[machine[0], machine[2]], [machine[1], machine[3]]])
    b = np.array(machine[4:])
    if part2:
        b += 10000000000000
    res = np.linalg.solve(a, b).round()
    if (a @ res == b).all():
        return int(res[0]) * 3 + int(res[1])
    return 0


print("A: ", sum(map(lambda m: cost(m), machines)))
print("B: ", sum(map(lambda m: cost(m, part2=True), machines)))
