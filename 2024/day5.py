from collections import defaultdict
from functools import cmp_to_key
from pathlib import Path

data = Path("2024/inputs/day5.txt").read_text().strip()


rules_data, pages = data.split("\n\n", maxsplit=1)

rules = defaultdict(list)

for rule in rules_data.splitlines():
    key, value = rule.split("|")
    rules[key].append(value)

page_lists = list(map(lambda line: line.split(","), pages.splitlines()))

print(len(rules))


def compare(x, y):
    if x in rules and y in rules[x]:
        return -1
    return 1


a_mids = []
b_mids = []
for pl in page_lists:
    sorted_pl = sorted(pl, key=cmp_to_key(compare))
    if sorted_pl == pl:
        a_mids.append(pl[len(pl) // 2])
    else:
        b_mids.append(sorted_pl[len(pl) // 2])


print("a", sum(map(int, a_mids)))
print("b", sum(map(int, b_mids)))
