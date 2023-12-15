from collections import defaultdict

data = open("./2021/day14/input.txt").read()
data = data.split("\n\n")
rows = list(map(lambda x: x.split(" -> "), data[1].splitlines()))

counts = defaultdict(lambda: 0)

tab = dict()
for r in rows:
    tab[r[0]] = r[1]

polymer = data[0]
for steps in range(10):
    newPoly = []
    c = 0
    while c < len(polymer) - 1:
        a = polymer[c]
        b = polymer[c + 1]
        if a + b in tab:
            newPoly.append(a + tab[a + b])
        c += 1
    newPoly.append(b)
    polymer = "".join(newPoly)
    print(steps + 1)

for i in polymer:
    counts[i] += 1

mx = list(counts.keys())[0]
mn = list(counts.keys())[0]
for k, v in counts.items():
    if v >= counts[mx]:
        mx = k
    if v < counts[mn]:
        mn = k

print(counts[mx] - counts[mn])

# good engough, better: 14b_T2.py with 10 instead of 40
