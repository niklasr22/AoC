from pathlib import Path
import re

input = Path("2024/inputs/day1.txt").read_text().strip().split("\n")

list1 = list(sorted([int(re.split(r"\s+", line)[0]) for line in input]))
list2 = list(sorted([int(re.split(r"\s+", line)[1]) for line in input]))

dists = [abs(a - b) for a, b in zip(list1, list2)]

print("a", sum(dists))

occurences = [a * list2.count(a) for a in list1]

print("b", sum(occurences))

