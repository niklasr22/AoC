import time

data = open("./2021/day7/input.txt").read()
crabs = list(map(int, data.split(",")))
minFuel = -1

start = time.time()


def test(h):
    f = 0
    for i in range(h + 1):
        f += i
    return f


for h in range(max(crabs) + 1):
    fuel = 0
    for c in crabs:
        fuel += test(abs(c - h))
    minFuel = min(fuel, minFuel) if minFuel > -1 else fuel
print(minFuel)
print(time.time() - start)
