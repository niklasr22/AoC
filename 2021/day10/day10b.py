data = open("./2021/day10/input.txt").read()
rows = list(data.splitlines())

opend = {"(": ")", "[": "]", "<": ">", "{": "}"}

scoret = {")": 1, "]": 2, "}": 3, ">": 4}

openc = opend.keys()
scores = []
for r in rows:
    q = []
    cor = False
    for c in r:
        if c in openc:
            q.append(opend[c])
        else:
            last = q.pop()
            if c != last:
                cor = True
                break
    if not cor and len(q) != 0:  # incomplete
        q.reverse()
        t = 0
        for c in q:
            t *= 5
            t += scoret[c]
        scores.append(t)
        print(t)

scores.sort()

print("scores", scores[len(scores) // 2])
