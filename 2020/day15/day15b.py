from collections import defaultdict

data = open("./2020/day15/input2.txt").read()
nbrs = list(map(int, data.split(",")))

nbt = defaultdict(lambda: [])

for i in range(len(nbrs)):
    nbt[nbrs[i]] = [i + 1]

turn = len(nbrs) + 1
last = nbrs[len(nbrs) - 1]
while turn <= 30000000:
    if nbt[last][0] == turn - 1:
        last = 0
        nbt[0].append(turn)
    else:
        i = nbt[last][0]
        if len(nbt[last]) > 1:
            nbt[last].pop(0)
        last = turn - 1 - i
        nbt[last].append(turn)
    turn += 1
print(turn - 1, last)
