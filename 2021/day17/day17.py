#test input
#targetX = (20, 30)
#targetY = (-10, -5)
#input
targetX = (209, 238)
targetY = (-86, -59)

def step(v, pp):
    pp[0] += v[0]
    pp[1] += v[1]
    if v[0] < 0:
        v[0] += 1
    elif v[0] > 0:
        v[0] -= 1
    v[1] -= 1

maxHOA = 0
count = 0
for vx in range(-targetX[1], targetX[1]+1):
    for vy in range(-abs(targetY[0]), abs(targetY[0])+1):
        v = [vx, vy]
        pp = [0,0]
        maxH = 0
        while True:
            step(v, pp)
            maxH = max(maxH,pp[1])
            if targetX[0] <= pp[0] <= targetX[1] and targetY[0] <= pp[1] <= targetY[1]:
                maxHOA = max(maxHOA,maxH)
                count += 1
                break
            if (pp[1] < targetY[0] and v[1] < 0) or (v[0] >= 0 and pp[0] > targetX[1]):
                break
print("a)", maxHOA)
print("b)", count)