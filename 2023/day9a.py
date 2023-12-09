from pathlib import Path


def next_val(reading: list[int]):
    diffs = [reading]
    while not all(diff == 0 for diff in diffs[-1]):
        new_diff = []
        for i in range(1, len(diffs[-1])):
            new_diff.append(diffs[-1][i] - diffs[-1][i - 1])
        diffs.append(new_diff)
    diffs[-1].append(0)
    for i in range(len(diffs) - 2, -1, -1):
        diffs[i].append(diffs[i][-1] + diffs[i + 1][-1])
    return diffs[0][-1]


readings = [
    list(map(int, x.split(" ")))
    for x in Path("2023/inputs/day9.txt").read_text().splitlines()
]

extrapolations = list(map(next_val, readings))
print(sum(extrapolations))
