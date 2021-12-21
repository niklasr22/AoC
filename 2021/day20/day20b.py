from collections import defaultdict

data = open('./2021/day20/input.txt').read()
data = data.split("\n\n")

algo = data[0]
image = data[1].splitlines()

img = defaultdict(lambda : ".")
wdt = len(image)
hgt = len(image[0])

for r in range(hgt):
    for c in range(wdt):
        img[(c,r)] = image[r][c]


h = [-1, 0, 1,  -1, 0, 1, -1, 0, 1]
v = [-1, -1, -1, 0, 0, 0, 1, 1, 1]

nextSpace = '.'
def enhace(input):
    global nextSpace
    img = defaultdict(lambda : nextSpace)
    left = min(input.keys(), key = lambda t: t[0])[0]
    right = max(input.keys(), key = lambda t: t[0])[0]
    top = min(input.keys(), key = lambda t: t[1])[1]
    bottom = max(input.keys(), key = lambda t: t[1])[1]

    for r in range(left-1, right + 2):
        for c in range(top-1, bottom + 2):
            bin = ""
            for i in range(9):
                x = c + h[i]
                y = r + v[i]
                bin += "1" if input[(x,y)] == "#" else "0"
            ind = int(bin, base=2)
            img[(c,r)] = algo[ind]
    nextSpace = img[(left-1,top-1)]
    return img

def printimg(res):
    left = min(res.keys(), key = lambda t: t[0])[0]
    right = max(res.keys(), key = lambda t: t[0])[0]
    top = min(res.keys(), key = lambda t: t[1])[1]
    bottom = max(res.keys(), key = lambda t: t[1])[1]

    for y in range(top, bottom + 1):
        row = ""
        for x in range(left, right + 1):
            row += res[(x,y)]
        print(row)

#printimg(img)
res = img
for i in range(50):
    res = enhace(res)

c = 0
for r in res.values():
    if r == "#":
        c+=1

print(c)