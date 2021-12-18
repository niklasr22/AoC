data = open("./2020/day9/input.txt").read()
xmas = list(map(int, data.splitlines()))


def check(x, data) -> bool:
    for i in range(25):
        for j in range(25):
            if data[i] + data[j] == x:
                return True
    return False

invalidNumber = -1
for i in range(25, len(xmas)):
    if not check(xmas[i], xmas[i - 25:i]):
        invalidNumber = xmas[i]
        break
print(xmas[i])

#b
for i in range(len(xmas)):
    for j in range(i + 2, len(xmas)):
        if sum(xmas[i:j]) == invalidNumber:
            print(min(xmas[i:j]) + max(xmas[i:j]))
            exit(0)