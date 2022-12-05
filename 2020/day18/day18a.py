data = open("./2020/day18/input.txt").read()
expressions = data.replace(" ", "").splitlines()


def solve(ex, t=0, p=False):
    if ex.find("*") == -1 and ex.find("+") == -1:
        return int(ex)
    if p:
        ex = ex[1 : len(ex) - 1]
    p = 0
    left = 0
    opi = -1
    op = ""
    for i in range(len(ex)):
        if p == 0:
            if ex[i] == "*" or ex[i] == "+":
                if opi != -1:
                    right = solve(ex[opi + 1 : i], t + 1, True)
                    left = left + right if op == "+" else left * right
                else:
                    left = solve(ex[:i], t + 1, True)
                opi = i
                op = ex[i]
        if ex[i] == "(":
            p += 1
        elif ex[i] == ")":
            p -= 1
    right = solve(ex[opi + 1 :], t + 1, True)
    left = left + right if op == "+" else left * right
    return left


exp_sum = 0
for ex in expressions:
    r = solve(ex)
    print("result", r)
    exp_sum += r
print(exp_sum)


"""

2 * 3 + (4 * 5)
5 + (8 * 3 + 9 + 3 * 4 * 3)
((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2
5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))

"""
