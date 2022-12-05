from collections import defaultdict

data = open("./2021/day20/input.txt").read()
data = data.split("\n\n")

algo = data[0]
image = data[1].splitlines()

img = defaultdict(lambda: ".")
wdt = len(image)
hgt = len(image[0])

for r in range(hgt):
    for c in range(wdt):
        img[(c, r)] = image[r][c]


h = [-1, 0, 1, -1, 0, 1, -1, 0, 1]
v = [-1, -1, -1, 0, 0, 0, 1, 1, 1]


def enhace(input, i=1):
    u = i
    z = "." if i == 0 else "#"
    img = defaultdict(lambda: ".")
    print(i, u, z, img[(0, 0)])
    i = 5
    print(i, u, z, img[(0, 1)])
    left = min(input.keys(), key=lambda t: t[0])[0]
    right = max(input.keys(), key=lambda t: t[0])[0]
    top = min(input.keys(), key=lambda t: t[1])[1]
    bottom = max(input.keys(), key=lambda t: t[1])[1]

    for r in range(left - 3, right + 4):
        for c in range(top - 3, bottom + 4):
            bin = ""
            for i in range(9):
                x = c + h[i]
                y = r + v[i]
                bin += "1" if input[(x, y)] == "#" else "0"
            ind = int(bin, base=2)
            """if c == 2 and r == 2:
                g = [input[(c-1,r-1)],input[(c,r-1)],input[(c+1,r-1)]]
                g1 = [input[(c-1,r)],input[(c,r)],input[(c+1,r)]]
                g2 = [input[(c-1,r+1)],input[(c,r+1)],input[(c+1,r+1)]]
                print(ind, g,g1,g2)"""
            img[(c, r)] = algo[ind]
    return img


def printimg(res):
    left = min(res.keys(), key=lambda t: t[0])[0]
    right = max(res.keys(), key=lambda t: t[0])[0]
    top = min(res.keys(), key=lambda t: t[1])[1]
    bottom = max(res.keys(), key=lambda t: t[1])[1]

    for y in range(top, bottom + 1):
        row = ""
        for x in range(left, right + 1):
            row += res[(x, y)]
        print(row)


# printimg(img)
res = enhace(img, 0)
# printimg(res)

res2 = enhace(res, 10000)
# printimg(res2)
c = 0
for r in res2.values():
    if r == "#":
        c += 1

print(c)
