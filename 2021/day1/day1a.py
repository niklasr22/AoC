file = open("./2021/day1/input.txt")
data = file.read()

rows = list(map(lambda x : int(x), filter(lambda x : x != '', data.split("\n"))))
c = 0
for i in range(1, len(rows)):
    if rows[i] != -1 and rows[i] > rows[i - 1]:
        c += 1

print("Increased", c, "times")