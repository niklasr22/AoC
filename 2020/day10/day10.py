data = open("./2020/day10/input.txt").read()
rows = list(map(int, data.splitlines()))
rows.sort()
rows.insert(0, 0)
rows.append(rows[len(rows) - 1] + 3)

jolt1 = 0
jolt3 = 0
for i in range(1, len(rows)):
    d = rows[i] - rows[i - 1]
    if d == 1:
        jolt1 += 1
    elif d == 3:
        jolt3 += 1
print("a", jolt3 * jolt1)

mem = {}


def otherPossR(rows, f, skipped=-1):
    if skipped in mem.keys():
        return mem[skipped]
    p = 0
    for i in range(len(rows) - 2, 0, -1):
        c = rows[i]
        n = rows[i + 1]
        if n - 3 <= rows[i - 1]:
            rows[i] = n
            poss = otherPossR(rows[: i + 1], f + 1, (c, n))
            mem[(c, n)] = poss
            p += 1 + poss
            rows[i] = c
    return p


poss = 1 + otherPossR(rows, 0)
print(poss)
