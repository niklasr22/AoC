data = open("./2021/day3/input.txt").read()
rows = data.splitlines()
ones = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
rowCountHalf = len(rows) / 2
d = 0

for r in rows:
    for i in range(len(r)):
        if r[i] == "1":
            ones[i] += 1

binGamma = ""
binEpsilon = ""
for i in ones:
    if i > rowCountHalf:
        binGamma += "1"
        binEpsilon += "0"
    else:
        binGamma += "0"
        binEpsilon += "1"

gamma = int(binGamma, base=2)
epsilon = int(binEpsilon, base=2)
print("binGamma", binGamma, gamma)
print("binEpsilon", binEpsilon, epsilon)
print("mult", gamma * epsilon)
