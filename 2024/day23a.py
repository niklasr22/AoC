import re
from pathlib import Path

data = Path("2024/inputs/day23.txt").read_text().strip()

computers = set(re.findall(r"([a-z]{2})", data))
connections = list(map(lambda x: x.split("-"), data.splitlines()))


connections_per_computer = {computer: set() for computer in computers}
for comp1, comp2 in connections:
    connections_per_computer[comp1].add(comp2)
    connections_per_computer[comp2].add(comp1)

t_computers = list(filter(lambda x: x.startswith("t"), computers))


groups = set()

for computer in t_computers:
    conns = connections_per_computer[computer]

    for other in conns:
        other_conns = connections_per_computer[other]

        common = other_conns.intersection(conns)
        for third in common:
            groups.add(tuple(sorted([computer, other, third])))
print(len(groups))
