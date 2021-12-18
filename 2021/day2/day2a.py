file = open("./2021/day2/input.txt")
data = file.read()

rows = list(map(lambda x : x.split(" "), filter(lambda x : x != '', data.split("\n"))))
x = 0
d = 0

for r in rows:
    if r[0] == "forward":
        x += int(r[1])
    elif r[0] == "up":
        d -= int(r[1])
    elif r[0] == "down":
        d += int(r[1])

print("Pos x", x, "d", d, "x*d", x*d)