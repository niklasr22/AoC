data = open("./2021/day7/input.txt").read()
crabs = list(map(int, data.split(",")))
minFuel = -1
for h in range(max(crabs) + 1):
    fuel = 0
    for c in crabs:
        fuel += abs(c - h)
    minFuel = min(fuel, minFuel) if minFuel > -1 else fuel
print(minFuel)
