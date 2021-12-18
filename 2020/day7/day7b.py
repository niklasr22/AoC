file = open("./2020/day7/input.txt")
data = file.read()

rules = data.splitlines()
colRules = dict()

for rule in rules:
    color, content = rule.split(" bags contain ")
    colRules[color] = list(map(lambda x : x.strip().split(" ", 1), content.replace("bags", "").replace("bag", "").replace(".", "").split(", ")))

def findChildBagCount(color, rules):
    count = 0
    for x, col in rules[color]:
        if x != "no":
            count += int(x) + int(x) * findChildBagCount(col, rules)
    return count

count = findChildBagCount("shiny gold", colRules)
print(count)