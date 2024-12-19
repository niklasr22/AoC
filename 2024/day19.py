from functools import cache
from pathlib import Path

data = Path("2024/inputs/day19.txt").read_text().strip()

available, designs = data.split("\n\n")

available = set(available.split(", "))
designs = designs.splitlines()


@cache
def check(design) -> bool:
    s = 0
    if design in available:
        s += 1

    for i in range(1, len(design)):
        if design[:i] not in available:
            continue
        s += check(design[i:])
    return s


results = [check(design) for design in designs]
print("A", sum(res > 0 for res in results))
print("B", sum(res for res in results))
