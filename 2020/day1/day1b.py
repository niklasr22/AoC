file = open("./2020/day1/input.txt")
data = file.read()

rows = list(map(lambda x : int(x), filter(lambda x : x != '', data.split("\n"))))

for i in range(len(rows)):
    for j in range(len(rows)):
        for h in range(len(rows)):
            if i != j and j != h and i != h and rows[i] + rows[j] + rows[h] == 2020:
                print(i, j, h, rows[i] * rows[j] * rows[h]);