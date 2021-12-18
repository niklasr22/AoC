data = open("./2020/day16/input.txt").read()
data = data.split("\n\n")

ruleList = list(map(lambda x: x.split(":"), data[0].splitlines()))
rules = dict()
for rule, ranges in ruleList:
    r1, r2 = ranges.split(" or ")
    r1 = r1.split("-")
    r2 = r2.split("-")
    rules[rule] = [range(int(r1[0]), int(r1[1]) + 1), range(int(r2[0]), int(r2[1]) + 1)]

myTicket = list(map(int, data[1].splitlines()[1].split(",")))
otherTickets = list(map(lambda x: list(map(int, x.split(","))), data[2].splitlines()[1:]))

scanningErrorRate = 0
for t in otherTickets:
    for v in t:
        f = False
        for k, r in rules.items():
            if v in r[0] or v in r[1]:
                f = True
                break
        if not f:
            scanningErrorRate += v
print(scanningErrorRate)