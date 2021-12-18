file = open("./2021/day1/input.txt")
data = file.read()

rows = list(map(lambda x : int(x), filter(lambda x : x != '', data.split("\n"))))
c = 0
i = 0
p = 0
while i + 3 <= len(rows):
    x = sum(rows[i:i+3])
    if i > 0 and p < x:
        c += 1
    p = x
    i += 1

print("Increased", c, "times")