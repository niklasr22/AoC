import statistics
data = open("./2021/day7/input.txt").read()
crabs = list(map(int, data.split(",")))
minFuel = -1
hm = int(statistics.mean(crabs))
for h in range(hm - 1, hm + 2):
    fuel = 0
    for c in crabs:
        w = abs(c - h)
        fuel += (w * (w + 1)) // 2
    minFuel = min(fuel, minFuel) if minFuel > -1 else fuel
print (minFuel)