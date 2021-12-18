data = open("./2020/day14/input.txt").read()
instructions = data.splitlines()
mem = dict()
mask = ""

def findAddresses(address, val, s):
    found = False
    for i in range(s, len(address)):
        if address[i] == 'X':
            found = True
            address[i] = '0'
            findAddresses(address, val, i + 1)
            address[i] = '1'
            findAddresses(address, val, i + 1)
            address[i] = 'X'
            break
    if not found:
        addr = "".join(address)
        mem[int(addr, 2)] = val

for i in instructions:
    if i.startswith("mask = "):
        mask = (i[7:])[::-1]
    else:
        address = format(int(i[4:i.find("]")]), 'b')[::-1]
        val = int(i[(i.find("=") + 1):])
        newAddress = ""
        j = 0
        l = len(address)
        for c in mask:
            if c == '0':
                newAddress += address[j] if j < l else '0'
            else:
                newAddress += c
            j += 1
        newAddress = list(newAddress)
        newAddress.reverse()
        findAddresses(newAddress, val, 0)
print(sum(mem.values()))