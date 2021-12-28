data = open("./2021/day2/input.txt").read()
rows = list(map(lambda x : x.split(" "), data.splitlines()))
x,d,a = 0,0,0
for c,i in rows:
    if c == "forward":
        x += int(i)
        d += a * int(i)
    elif c == "up":
        a -= int(i)
    elif c == "down":
        a += int(i)

print(x * d)