file = open("./2020/day1/input.txt")
data = file.read()

rows = list(map(lambda x: int(x), filter(lambda x: x != "", data.split("\n"))))

for i in range(len(rows)):
    for j in range(len(rows)):
        if i != j and rows[i] + rows[j] == 2020:
            print(i, j, rows[i] * rows[j])
