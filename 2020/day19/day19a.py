data = open("./2020/day19/input.txt").read()
data = data.split("\n\n")
rulesL = data[0].splitlines()
rules = {}
for r in rulesL:
    k, v = r.split(": ")
    rules[k] = list(map(lambda y: y.replace('"', "").split(" "), v.split(" | ")))
    if len(rules[k]) == 1 and len(rules[k][0]) == 1 and not rules[k][0][0].isnumeric():
        rules[k] = rules[k][0][0]

print(rules)

msgs = data[1].splitlines()


def validateMsg(msg, rk, t=0):
    ruleSet = rules[rk]
    if type(ruleSet) == str:
        if msg[0] == ruleSet:
            return True, msg[1:]
        else:
            return False, msg

    for rule in ruleSet:
        ruleValid = True
        mc = msg
        for i in rule:
            ruleValid, m = validateMsg(mc, i, t + 1)
            mc = m
            if not ruleValid:
                break
        if ruleValid:
            return True, mc

    return False, msg


count = 0
for msg in msgs:
    v, m = validateMsg(msg, "0")
    v = v and len(m) == 0 if v else v
    print(msg, v)
    if v:
        count += 1
print(count)
