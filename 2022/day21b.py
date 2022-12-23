import aocutils

monkeys = {
    m[0]: int(m[1]) if m[1].isnumeric() else m[1].split(" ")
    for m in aocutils.read_lines("./2022/inputs/day21.txt", lambda x: x.split(": "))
}


def calc(operation, op1, op2):
    if operation == "+":
        return op1 + op2
    elif operation == "*":
        return op1 * op2
    elif operation == "/":
        return int(op1 / op2)
    elif operation == "-":
        return op1 - op2


def solve(m) -> int:
    if type(monkeys[m]) == int:
        return monkeys[m]
    formular = monkeys[m]
    op1 = solve(formular[0])
    op2 = solve(formular[2])
    res = calc(formular[1], op1, op2)
    return res


def contains_humn(m):
    if m == "humn":
        return True
    if type(monkeys[m]) == int:
        return False
    formular = monkeys[m]
    return (
        formular[0] == "humn"
        or formular[2] == "humn"
        or contains_humn(formular[0])
        or contains_humn(formular[2])
    )


if contains_humn(monkeys["root"][0]):
    eq = solve(monkeys["root"][2])
    op = monkeys["root"][0]
else:
    eq = solve(monkeys["root"][0])
    op = monkeys["root"][2]

op_inv1 = {"+": "-", "-": "+", "/": "*", "*": "/"}
op_inv2 = {"+": "-", "-": "-", "/": "/", "*": "/"}


def solve2(target, m):
    if m == "humn":
        return target

    formular = monkeys[m]
    if contains_humn(formular[0]):
        op = formular[0]
        target = calc(op_inv1[formular[1]], target, solve(formular[2]))
    else:
        op = formular[2]
        inv_operands = formular[1] == "*" or formular[1] == "+"
        target = calc(
            op_inv2[formular[1]],
            target if inv_operands else solve(formular[0]),
            solve(formular[0]) if inv_operands else target,
        )
    return solve2(target, op)


print(solve2(eq, op))
