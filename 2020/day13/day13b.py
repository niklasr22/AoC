data = open("./2020/day13/input.txt").read()
data = data.splitlines()

earliest = int(data[0])
busses = list(map(lambda x: int(x) if x != "x" else -1, data[1].split(",")))

maxB = max(busses)
maxBi = busses.index(maxB)
print(maxB, maxBi)


def mult(x):
    r = 1
    for i in x:
        r *= i
    return r


def gcdExtended(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = gcdExtended(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y


# chinese
tups = []
o = 0
m = 1
for i in busses:
    if i != -1:
        m *= i
        tups.append((i, o))
    o -= 1
x = 0
for i in tups:
    mi = m / i[0]
    gcd, a, b = gcdExtended(i[0], mi)
    ei = i[1] * b * mi
    x += ei

mod = int(x) % m
print(mod)

# brute force
"""s = False
t = 1
#i = 100000000000000 // maxB
#i = 1068784 // maxB
i = 0
while True:
    i += 1
    t = i * maxB - maxBi
    x = 0
    v = True
    for b in busses:
        if b != -1:
            if (t + x) % b != 0:
                v = False
                break
        x += 1
    if v:
        print("Erg", t)
        x = 0
        for b in busses:
            if b != -1:
                print(t, t + x, b, (t + x) % b)
            else:
                print(t, t + x, b, "xxx")
            x += 1
        break"""
