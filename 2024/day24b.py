from pathlib import Path

data = Path("2024/inputs/day24.txt").read_text().strip()

init_vals, connections = data.split("\n\n")
vals = dict(
    map(lambda x: (x.split(": ")[0], int(x.split(": ")[1])), init_vals.splitlines())
)

connections = list(
    map(lambda x: x.replace(" -> ", " ").split(" "), connections.splitlines())
)


def sim(connections, vals):
    queue = connections.copy()
    vals = vals.copy()
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
        for i, k in enumerate(
            sorted([key for key in vals.keys() if key.startswith("z")])
        )
    ]
    return sum(z_vals)


def ints_to_vals(x, y):
    x = {"x{0:02}".format(i): int((x & (1 << i)) > 0) for i in range(45)}
    y = {"y{0:02}".format(i): int((y & (1 << i)) > 0) for i in range(45)}
    x.update(y)
    return x


def find_op(ops, op):
    for o in ops:
        if o[:3] == op or o[:3][::-1] == op:
            return o
    return None


def find_missing_in(ops, in1, op, target):
    for o in ops:
        if o[1] == op:
            if target is not None:
                if o[3] != target:
                    continue

            if o[0] == in1:
                return o
            elif o[2] == in1:
                return o
    return None


def bottom_up(target):
    tidx = int(target[1:])
    deps = connections

    start = find_op(deps, ["x{0:02}".format(0), "AND", "y{0:02}".format(0)])
    if start is None and tidx > 0:
        print("missing", "start", ["x00", "AND", "y00"])
        return False, (["x{0:02}".format(0), "AND", "y{0:02}".format(0)], None)

    end = find_op(deps, ["x{0:02}".format(tidx), "XOR", "y{0:02}".format(tidx)])
    if end is None:
        print("missing", "end", ["x{0:02}".format(tidx), "XOR", "y{0:02}".format(tidx)])
        return False, (["x{0:02}".format(tidx), "XOR", "y{0:02}".format(tidx)], None)

    if tidx == 0:
        return True, None

    prev = start
    for i in range(1, tidx):
        and_op_in = ["x{0:02}".format(i), "AND", "y{0:02}".format(i)]
        xor_op_in = ["x{0:02}".format(i), "XOR", "y{0:02}".format(i)]
        and_op = find_op(deps, and_op_in)
        xor_op = find_op(deps, xor_op_in)

        if and_op is None:
            print("missing", "and_op", i, and_op_in)
            return False, (and_op_in, None)

        if and_op[3].startswith("z"):
            print("wrong output", "and_op", i, and_op_in)
            return False, (and_op_in, None)

        if xor_op[3].startswith("z"):
            print("wrong output", "xor_op", i, xor_op_in)
            return False, (xor_op_in, None)

        if xor_op is None:
            print("missing", "xor_op", i, xor_op_in)
            return False, (xor_op_in, None)

        required_and_in = [prev[3], "AND", xor_op[3]]
        required_and = find_op(deps, required_and_in)
        if required_and is None:
            print("missing", "required_and", i, required_and_in)
            return False, (required_and_in, None)

        if required_and[3].startswith("z"):
            print("wrong output", "required_and", i, required_and_in)
            return False, (required_and_in, None)

        required_or_in = [required_and[3], "OR", and_op[3]]
        required_or = find_op(deps, required_or_in)
        if required_or is None:
            print("missing", "required_or", i, required_or_in)
            print(find_missing_in(connections, required_and[3], "OR", None))
            print(find_missing_in(connections, and_op[3], "OR", None))
            return False, (required_or_in, None)

        if required_or[3].startswith("z"):
            print("wrong output", "required_or", i, required_or_in)
            print(find_missing_in(connections, required_and[3], "OR", None))
            print(find_missing_in(connections, and_op[3], "OR", None))
            return False, (required_or_in, None)

        prev = required_or

    final_xor_in = [prev[3], "XOR", end[3]]
    final_xor = find_op(deps, final_xor_in)
    if final_xor is None:
        fixes = find_missing_in(connections, prev[3], "XOR", target)
        if fixes is None:
            fixes = find_missing_in(connections, end[3], "XOR", target)[2]
        else:
            fixes = fixes[0]

        print("missing", "final_xor", final_xor_in, "fix", fixes)
        print("correct", end)
        return False, (
            end,
            fixes,
        )
    if final_xor[3] != target:
        print("final_xor", final_xor, "expected", target)
        return False, (final_xor, target)
    return True, None


swaps = set()
for z in range(45):
    z = "z{0:02}".format(z)
    res, wrong = bottom_up(z)
    if not res:
        wrong, fix = wrong
        print("failed", z, wrong, "fix", fix)

        if wrong:
            if fix is None:
                break

            # fix issue
            i1 = connections.index(wrong)

            other = list(filter(lambda x: x[3] == fix, connections))[0]
            i2 = connections.index(other)

            fixed = wrong.copy()
            fixed[3] = fix
            connections[i1] = fixed

            other_fixed = other.copy()
            other_fixed[3] = wrong[3]
            connections[i2] = other_fixed

            swaps.add(fix)
            swaps.add(wrong[3])
print(",".join(sorted(list(swaps))))
