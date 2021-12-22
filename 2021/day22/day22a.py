from collections import defaultdict

data = open("./2021/day22/input.txt").read()
rows = list(map(lambda x : (x.split(" ")[0], [list(map(int, z.split("=")[1].split(".."))) for z in x[3:].split(",")]), data.splitlines()))
#print(rows)

grid = defaultdict(lambda:0)

for m,r in rows:
    xrange = range(r[0][0] if r[0][0] >= -50 else -50, r[0][1] + 1 if r[0][1] <= 50 else 51)
    yrange = range(r[1][0] if r[1][0] >= -50 else -50, r[1][1] + 1 if r[1][1] <= 50 else 51)
    zrange = range(r[2][0] if r[2][0] >= -50 else -50, r[2][1] + 1 if r[2][1] <= 50 else 51)
    for z in zrange:
        for y in yrange:
            for x in xrange:
                if m == "on":
                    grid[(x,y,z)] = 1
                else:
                    grid[(x,y,z)] = 0

print(sum(grid.values()))
