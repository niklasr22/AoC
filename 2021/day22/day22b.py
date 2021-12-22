data = open("./2021/day22/input.txt").read()
rows = list(map(lambda x : (x.split(" ")[0], [list(map(int, z.split("=")[1].split(".."))) for z in x[3:].split(",")]), data.splitlines()))
#print(rows)

cubes = []
for m,r in rows:
    x,y,z,xx,yy,zz = (r[0][0], r[1][0], r[2][0], r[0][1], r[1][1], r[2][1])

    newCubes = []
    #remove intersections (with new cube)
    for cu in cubes:
        a,b,c,aa,bb,cc = cu
        if xx < a or aa < x or yy < b or bb < y or zz < c or cc < z: #no intersection
            newCubes.append(cu)
            continue
        if x > a:
            newCubes.append((a, b, c, x - 1, bb, cc))
        if xx < aa:
            newCubes.append((xx + 1, b, c, aa, bb, cc))
        if y > b:
            newCubes.append((max(a,x), b, c, min(aa,xx), y - 1, cc))
        if yy < bb:
            newCubes.append((max(a,x), yy + 1, c, min(aa,xx), bb, cc))
        if z > c:
            newCubes.append((max(a,x), max(b,y), c, min(aa,xx), min(bb,yy), z - 1))
        if zz < cc:
            newCubes.append((max(a,x), max(b,y), zz + 1, min(aa,xx), min(bb,yy), cc))
    if m == "on":
        newCubes.append((min(x,xx), min(y,yy), min(z,zz), max(x,xx), max(y,yy), max(z,zz)))
    cubes = newCubes

vol = 0
for c in cubes:
    vol += (c[3] + 1 - c[0]) * (c[4] + 1 - c[1]) * (c[5] + 1 - c[2])

print(vol)
