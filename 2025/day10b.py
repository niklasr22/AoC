import re
from pathlib import Path

import z3

data = Path("2025/inputs/day10.txt").read_text().strip()

result = 0
for line in data.splitlines():
    joltageRegex = re.compile(r"\{([0-9,]+)\}")
    joltages = list(
        map(int, str(joltageRegex.search(line).group(0)).strip("{}").split(","))
    )

    btnRegex = re.compile(r"\(([0-9,]+)\)")
    btns = list(map(lambda b: list(map(int, b.split(","))), btnRegex.findall(line)))

    btnInds = [[1 if i in btn else 0 for i in range(len(joltages))] for btn in btns]

    solver = z3.Optimize()
    x = z3.IntVector("x", len(btnInds))
    for j in range(len(joltages)):
        lhs = sum(b[j] * x[bi] for bi, b in enumerate(btnInds))
        solver.add(lhs == joltages[j])

    for i in range(len(btnInds)):
        solver.add(x[i] >= 0)

    h = solver.minimize(z3.Sum(x))

    res = solver.check()
    if res == z3.sat:
        res = solver.model()
        result += sum([res[x_v].as_long() for x_v in x])
    else:
        print("failed")
print(result)
