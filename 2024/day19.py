from functools import cache
from pathlib import Path

data = Path("2024/inputs/day19.txt").read_text().strip()

patterns, designs = data.split("\n\n")

patterns = set(patterns.split(", "))
designs = designs.splitlines()


@cache
def check(design) -> bool:
    s = 0
    if design in patterns:
        s += 1

    for i in range(1, len(design)):
        if design[:i] not in patterns:
            continue
        s += check(design[i:])
    return s


results = [check(design) for design in designs]
print("A", sum(res > 0 for res in results))
print("B", sum(res for res in results))
