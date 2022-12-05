data = open("./2020/day14/input.txt").read()
instructions = data.splitlines()

mem = dict()

mask = "X" * 37
for i in instructions:
    if i.startswith("mask = "):
        mask = (i[7:])[::-1]
    else:
        address = i[4 : i.find("]")]
        val = format(int(i[(i.find("=") + 1) :]), "b")[::-1]
        newVal = ""
        j = 0
        l = len(val)
        for c in mask:
            if c == "X":
                newVal += val[j] if j < l else "0"
            else:
                newVal += c
            j += 1
        # print(address, i[(i.find("=") + 1):], int(newVal[::-1], 2))
        mem[address] = int(newVal[::-1], 2)

print(sum(mem.values()))
