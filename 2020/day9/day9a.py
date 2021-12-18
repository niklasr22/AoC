data = open("./2020/day9/input.txt").read()
xmas = list(map(int, data.splitlines()))


def check(x, data) -> bool:
    for i in range(25):
        for j in range(25):
            if data[i] + data[j] == x:
                return True
    return False

for i in range(25, len(xmas)):
    if not check(xmas[i], xmas[i - 25:i]):
        print(xmas[i])
        break
