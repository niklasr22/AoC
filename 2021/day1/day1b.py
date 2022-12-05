data = open("./2021/day1/input.txt").read()
rows = list(map(int, data.splitlines()))
c, i, p = 0, 0, 0
while i + 3 <= len(rows):
    x = sum(rows[i : i + 3])
    c += i > 0 and p < x
    p = x
    i += 1
print("Increased", c, "times")
