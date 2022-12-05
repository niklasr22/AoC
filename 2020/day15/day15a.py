data = open("./2020/day15/input2.txt").read()
nbrs = list(map(int, data.split(",")))

turn = len(nbrs)
while turn < 30000000:
    last = nbrs[turn - 1]
    try:
        i = nbrs.index(last)
        if turn - 1 == i:
            raise ValueError
        nbrs.append(turn - 1 - i)
        try:
            x = nbrs.index(last, i)
            nbrs[i] = -1
        except ValueError:
            pass
    except ValueError:
        nbrs.append(0)
    turn += 1
print(turn, nbrs[len(nbrs) - 1], "last", last)
