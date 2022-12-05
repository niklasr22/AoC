file = open("./2020/day7/input.txt")
data = file.read()

rules = data.splitlines()
colRules = dict()

for rule in rules:
    color, content = rule.split(" bags contain ")
    colRules[color] = content.split(", ")


def hasBagColor(color, content):
    for c in content:
        if c.find(color) != -1:
            return True
    return False


def findWrapper(color, rules, validRules):
    c = 0
    for rule, content in rules.items():
        if hasBagColor(color, content):
            validRules.add(rule)
            c += 1 + findWrapper(rule, colRules, validRules)
    return c


count = 0
validRules = set()
for rule, content in colRules.items():
    if hasBagColor("shiny gold", content):
        validRules.add(rule)
        count += 1 + findWrapper(rule, colRules, validRules)
print(len(validRules))
