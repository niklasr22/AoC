data = open("./2021/day2/input.txt").read()
rows = list(map(lambda x : x.split(" "), data.splitlines()))
x,d = 0,0
for c,i in rows:
    if c == "forward":
        x += int(i)
    elif c == "up":
        d -= int(i)
    elif c == "down":
        d += int(i)
print(x * d)