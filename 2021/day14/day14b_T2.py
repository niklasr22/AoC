from collections import Counter

data = open("./2021/day14/input.txt").read()
data = data.split("\n\n")
polymer = data[0]
tab = {p: m for p, m in list(map(lambda x: x.split(" -> "), data[1].splitlines()))}

counter = Counter([tuple(polymer[i : i + 2]) for i in range(len(polymer) - 1)])
for steps in range(100):
    newCounter = Counter()
    for c in counter:
        a, b = c
        x = tab[a + b]
        newCounter[a + x] += counter[c]
        newCounter[x + b] += counter[c]
    counter = newCounter

countLetters = Counter()
for c in counter:
    a, b = c
    countLetters[a] += counter[
        c
    ]  # add count only to counts[a] because in another iteration b will be a.
countLetters[polymer[-1]] += 1  # only the last b needs to be added manually
mx = max(countLetters.values())
mn = min(countLetters.values())
print(mx - mn)
