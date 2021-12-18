data = open('./2021/day16/input2.txt').read()
bits = ""
for b in data:
    x = '{0:b}'.format(int(b, base=16))
    bits += ('0' * (4 - len(x) % 4)) + x if len(x) % 4 != 0 else x
versionCounter = 0
print(bits)

def readPackage(bits):
    global versionCounter
    v = int(bits[:3], base=2)
    t = int(bits[3:6], base=2)
    versionCounter += v
    if t == 4:
        lastI = 0
        number = ''
        for i in range(6, len(bits), 5):
            group = bits[i:i+5]
            number += group[1:]
            if group[0] == '0':
                lastI = i + 5
                break
        return bits[lastI:], int(number, base=2)
    else:
        operands = []
        result = 1
        if bits[6] == '0':
            length = int(bits[7:22], base=2)
            bitslength = len(bits) - 22
            b = bits[22:]
            while bitslength - len(b) < length and len(b) != 0:
                b,x = readPackage(b)
                operands.append(x)
        else:
            packs = int(bits[7:18], base=2)
            b = bits[18:]
            for _ in range(packs):
                b,x = readPackage(b)
                operands.append(x)
                if len(b) == "":
                    break
        if t == 0:
            result = sum(operands)
        elif t == 1:
            for o in operands:
                result *= o
        elif t == 2:
            result = min(operands)
        elif t == 3:
            result = max(operands)
        elif t == 5:
            result = 1 if operands[0] > operands[1] else 0
        elif t == 6:
            result = 1 if operands[0] < operands[1] else 0
        elif t == 7:
            result = 1 if operands[0] == operands[1] else 0
        return b, result

res = readPackage(bits)[1]
print('a)', versionCounter)
print('b)', res)