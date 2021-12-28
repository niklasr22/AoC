data = open("./2021/day1/input.txt").read()
rows = list(map(int, data.splitlines()))
c = 0
for i in range(1, len(rows)):
    c += rows[i] > rows[i - 1]
print("Increased", c, "times")