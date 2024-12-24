from pathlib import Path

data = Path("2024/inputs/day24.txt").read_text().strip()

init_vals, connections = data.split("\n\n")
vals = dict(
    map(lambda x: (x.split(": ")[0], int(x.split(": ")[1])), init_vals.splitlines())
)

connections = list(
    map(lambda x: x.replace(" -> ", " ").split(" "), connections.splitlines())
)

queue = connections
while queue:
    a, op, b, target = queue.pop(0)
    if a not in vals or b not in vals:
        queue.append([a, op, b, target])
        continue

    if op == "AND":
        vals[target] = vals[a] & vals[b]
    elif op == "OR":
        vals[target] = vals[a] | vals[b]
    elif op == "XOR":
        vals[target] = vals[a] ^ vals[b]
    else:
        raise ValueError(f"Unknown op: {op}")

z_vals = [
    vals[k] * 2**i
    for i, k in enumerate(sorted([key for key in vals.keys() if key.startswith("z")]))
]
print(sum(z_vals))
