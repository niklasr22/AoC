data = open("./2021/day10/input.txt").read()
rows = list(data.splitlines())

opend = {"(": ")", "[": "]", "<": ">", "{": "}"}

scoret = {")": 3, "]": 57, "}": 1197, ">": 25137}

openc = opend.keys()

score = 0
for r in rows:
    q = []
    l = ""
    for c in r:
        if c in openc:
            q.append(opend[c])
        else:
            last = q.pop()
            if c != last:
                score += scoret[c]
                # print("corrupted", r, q,last, c)
                break

print(score)
