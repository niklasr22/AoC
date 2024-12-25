from pathlib import Path

import numpy as np

data = (
    Path("2024/inputs/day25.txt")
    .read_text()
    .strip()
    .replace("#", "1")
    .replace(".", "0")
)

key_lock_objs = [obj.splitlines() for obj in data.split("\n\n")]


locks = [
    np.array([list(map(int, list(line))) for line in obj]).sum(axis=0) - 1
    for obj in key_lock_objs
    if "0" not in obj[0]
]
keys = [
    np.array([list(map(int, list(line))) for line in obj]).sum(axis=0) - 1
    for obj in key_lock_objs
    if "0" not in obj[-1]
]

combinations = 0
full = np.ones(5) * 5
for lock in locks:
    for key in keys:
        if np.all(key + lock <= full):
            combinations += 1
print(combinations)
