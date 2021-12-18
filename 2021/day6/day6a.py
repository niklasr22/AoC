#großer pfusch, besser b
file = open("./2021/day6/input.txt")
data = file.read()
fishes = list(map(int, data.split(",")))
newFishes = []
for i in range(80):
    newFishes = []
    print(i)
    for x in range(len(fishes)):
        if fishes[x] == 0:
            newFishes.append(8)
            fishes[x] = 6
        else:
            fishes[x] -= 1
    fishes += newFishes
print(len(fishes))