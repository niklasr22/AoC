data = open("./2021/day8/input.txt").read()
rows = list(map(lambda x : x.split(" | "), data.splitlines()))

count = 0
for r in rows:
    digits = r[1].split(" ")
    print(digits)
    for d in digits:
        if len(d) == 2 or len(d) == 4 or len(d) == 7 or len(d) == 3:
            count += 1

print(count)