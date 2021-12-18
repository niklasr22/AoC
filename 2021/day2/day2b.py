file = open("./2021/day2/input.txt")
data = file.read()

rows = list(map(lambda x : x.split(" "), filter(lambda x : x != '', data.split("\n"))))
x = 0
d = 0
a = 0

for r in rows:
    if r[0] == "forward":
        x += int(r[1])
        d += a * int(r[1])
    elif r[0] == "up":
        a -= int(r[1])
    elif r[0] == "down":
        a += int(r[1])

print("Pos x", x, "d", d, "x*d", x*d)