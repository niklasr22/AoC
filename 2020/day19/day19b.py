data = open("./2020/day19/input3.txt").read()
data = data.split("\n\n")
rulesL = data[0].splitlines()
rules = {}
for r in rulesL:
    k,v = r.split(": ")
    rules[k] = list(map(lambda y : y.replace('"',"").split(" "), v.split(" | ")))
    if len(rules[k]) == 1 and len(rules[k][0]) == 1 and not rules[k][0][0].isnumeric():
        rules[k] = rules[k][0][0]

rules['8'] = [['42'],['42','8']]
rules['11'] = [['42', '31'],['42','11','31']]

print(rules)

msgs = data[1].splitlines()

def validateMsg(msg, rk,t=0):
    ruleSet = rules[rk]
    print("\t"*t, "check msg",msg, rk)

    if type(ruleSet) == str:
        if len(msg) > 0 and msg[0] == ruleSet:
            print("\t"*t, "isvalid", True)     
            return True, msg[1:]
        else:
            print("\t"*t, "isvalid", False)     
            return False, msg

    for rule in ruleSet:
        ruleValid = True
        mc = msg
        print("\t"*t, "next rule")
        for i in rule:
            ruleValid,m = validateMsg(mc, i, t+1)
            mc = m
            if not ruleValid:
                break
        if ruleValid:
            print("\t"*t, "isvalid", True)  
            return True, mc
       
    print("\t"*t, "isvalid", False)             
    return False, msg

count = 0
for msg in msgs:
    v, m = validateMsg(msg, "0")
    v = v and len(m) == 0 if v else v
    print(msg, v)
    if v:
        count += 1
print(count)