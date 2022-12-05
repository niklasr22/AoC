# ewwwwwwww
data = open("./2020/day18/input.txt").read()
expressions = data.replace(" ", "").splitlines()


def solve(ex: str, t=0):
    if ex.isnumeric():
        return int(ex)
    if ex[0]:
        p = 0
        continuosParantheses = True
        for i in range(len(ex)):
            if ex[i] == "(":
                p += 1
            elif ex[i] == ")":
                p -= 1
            if p == 0 and i != len(ex) - 1:
                continuosParantheses = False
        if continuosParantheses:
            ex = ex[1 : len(ex) - 1]
    exsplit = []
    lastCut = 0
    appendEnd = True
    p = 0
    for i in range(len(ex)):
        if p == 0:
            if ex[i] == "+":
                exsplit.append(solve(ex[lastCut:i], t + 1))
                exsplit.append(ex[i])
                lastCut = i + 1
            elif ex[i] == "*":
                exsplit.append(solve(ex[lastCut:i], t + 1))
                exsplit = [exsplit, ex[i], solve(ex[i + 1 :], t + 1)]
                appendEnd = False
                lastCut = i + 1
                break
        if ex[i] == "(":
            p += 1
        elif ex[i] == ")":
            p -= 1
    if appendEnd:
        exsplit.append(solve(ex[lastCut:]))

    return exsplit


def calc(exp, t=0):
    if not isinstance(exp, list):
        return exp
    else:
        if len(exp) == 1:
            return calc(exp[0], t + 1)

    if len(exp) > 3:
        res = 0
        for i in exp:
            if i != "+":
                res += calc(i, t + 1)
        return res

    left = 0
    if isinstance(exp[0], list):
        if len(exp[0]) == 1:
            if isinstance(exp[0][0], list):
                left = calc(exp[0][0], t + 1)
            else:
                left = exp[0][0]
        else:
            left = calc(exp[0], t + 1)
    else:
        left = exp[0]
    right = 0
    if isinstance(exp[2], list):
        if len(exp[2]) == 1:
            if isinstance(exp[2][0], list):
                right = calc(exp[2][0], t + 1)
            else:
                right = exp[2][0]
        else:
            right = calc(exp[2], t + 1)
    else:
        right = exp[2]
    if exp[1] == "*":
        return left * right
    else:
        return left + right


exp_sum = 0
for ex in expressions:
    r = solve(ex)
    res = calc(r)
    print("result", res)
    exp_sum += res
print(exp_sum)


"""

2 * 3 + (4 * 5)
5 + (8 * 3 + 9 + 3 * 4 * 3)
((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2
5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))

"""
