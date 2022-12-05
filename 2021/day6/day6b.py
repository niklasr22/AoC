file = open("./2021/day6/input.txt")
data = file.read()
fishes = list(map(int, data.split(",")))
fishcount = len(fishes)
fc = [0] * 9
for i in fishes:
    fc[i] += 1
for i in range(256):
    newFc = [0] * 9
    for x in range(0, 9):
        if x == 0:
            newFc[8] = fc[0]
            newFc[6] += fc[0]
        else:
            newFc[x - 1] += fc[x]
    fc = newFc
print(sum(fc))
