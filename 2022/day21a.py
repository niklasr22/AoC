import aocutils

monkeys = {
    m[0]: int(m[1]) if m[1].isnumeric() else m[1].split(" ")
    for m in aocutils.read_lines("./2022/inputs/day21.txt", lambda x: x.split(": "))
}


def solve(m) -> int:
    if type(monkeys[m]) == int:
        return monkeys[m]
    formular = monkeys[m]
    op1 = solve(formular[0])
    op2 = solve(formular[2])
    if formular[1] == "+":
        res = op1 + op2
    elif formular[1] == "*":
        res = op1 * op2
    elif formular[1] == "/":
        res = int(op1 / op2)
    elif formular[1] == "-":
        res = op1 - op2
    # monkeys[m] = res
    return res


print(solve("root"))
