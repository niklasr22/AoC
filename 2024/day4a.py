from pathlib import Path

import numpy as np

input = Path("2024/inputs/day4.txt").read_text().strip().splitlines()

XMAS = np.array(list("XMAS"))
XMAS_REV = np.array(list("SAMX"))


def diag_search(sm_matrix):
    count = 0
    if (np.diag(sm_matrix) == XMAS).all() or (np.diag(sm_matrix) == XMAS_REV).all():
        count += 1

    if (np.diag(sm_matrix[:, ::-1]) == XMAS).all() or (
        np.diag(sm_matrix[:, ::-1]) == XMAS_REV
    ).all():
        count += 1

    return count


matrix = np.array([list(x) for x in input])
xmas_count = 0
for y in range(0, len(matrix) - 3):
    for x in range(0, len(matrix[y]) - 3):
        sm_matrix = matrix[y : y + 4, x : x + 4]
        xmas_count += diag_search(sm_matrix)

for y in range(0, len(matrix)):
    for x in range(0, len(matrix[y]) - 3):
        xmas_count += (matrix[y, x : x + 4] == XMAS).all() + (
            matrix[y, x : x + 4] == XMAS_REV
        ).all()

for x in range(0, len(matrix[0])):
    for y in range(0, len(matrix) - 3):
        xmas_count += (matrix[y : y + 4, x] == XMAS).all() + (
            matrix[y : y + 4, x] == XMAS_REV
        ).all()

print(xmas_count)
