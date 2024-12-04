from pathlib import Path

import numpy as np

input = Path("2024/inputs/day4.txt").read_text().strip().splitlines()

MAS = np.array(list("MAS"))
MAS_REV = np.array(list("SAM"))


def search_3x3(sm_matrix):
    if (
        (np.diag(sm_matrix[:, ::-1]) == MAS).all()
        or (np.diag(sm_matrix[:, ::-1]) == MAS_REV).all()
    ) and ((np.diag(sm_matrix) == MAS).all() or (np.diag(sm_matrix) == MAS_REV).all()):
        return 1
    return 0


matrix = np.array([list(x) for x in input])
x_count = 0
for y in range(0, len(matrix) - 2):
    for x in range(0, len(matrix[y]) - 2):
        x_count += search_3x3(matrix[y : y + 3, x : x + 3])

print(x_count)
