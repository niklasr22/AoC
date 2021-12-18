from collections import defaultdict
data = open("./2021/day14/input2.txt").read()
data = data.split("\n\n")
rows = list(map(lambda x : x.split(" -> "), data[1].splitlines()))
polymer = data[0]

counts = defaultdict(lambda:0)

tab = dict()
for r in rows:
    tab[r[0]] = r[1]

for c in polymer:
    counts[c] += 1

def rek(a:str, b:str, i:int):
    if i <= 0:
        return
    if a + b in tab:
        counts[tab[a + b]] += 1
        rek(a, tab[a + b], i - 1)
        rek(tab[a + b], b, i - 1)

c = 0
while c < len(polymer) - 1:
    a = polymer[c]
    b = polymer[c+1]
    print(a,b)
    rek(a, b, 40)
    c += 1

mx = list(counts.keys())[0]
mn = list(counts.keys())[0]
for k, v in counts.items():
    if v >= counts[mx]:
        mx = k
    if v < counts[mn]:
        mn = k

print(counts[mx] - counts[mn])

#epic fail