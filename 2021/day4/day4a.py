data = open("./2021/day4/input.txt").read()

x = data.split("\n", maxsplit=1)
numbers = x[0].split(",")

x[1] = x[1].strip(" \n")

fields = list(map(lambda g: [0, g], list(map(lambda c: c.split(), x[1].split("\n\n")))))


def printfield(field):
    for i in range(5):
        print(field[i * 5 : i * 5 + 5])


def score(field):
    score = 0
    for i in field:
        if i != "x":
            score += int(i)
    return score


def test(field):
    for i in range(5):
        h = 0
        v = 0
        for j in range(5):
            if field[i * 5 + j] != "x":
                h += 1
            if field[j * 5 + i] != "x":
                v += 1
        if h == 0 or v == 0:
            return True
    return False


def check(field, number):
    for i in range(len(field)):
        if field[i] == number:
            field[i] = "x"
    return test(field)


last = None
for a in numbers:
    for f in fields:
        if f[0] == 0 and check(f[1], a):
            f[0] = 1
            s = score(f[1]) * int(a)
            printfield(f[1])
            print(a, s)
            last = f
