data = open("./2021/day9/input.txt").read()
rows = list(data.splitlines())

riskLevel = 0

for y in range(len(rows)):
    for x in range(len(rows[y])):
        up = int(rows[y - 1][x]) if y > 0 else 10
        down = int(rows[y + 1][x]) if y < len(rows) - 1 else 10
        left = int(rows[y][x - 1]) if x > 0 else 10
        right = int(rows[y][x + 1]) if x < len(rows[y]) - 1 else 10

        pos = int(rows[y][x])
        if pos < up and pos < down and pos < left and pos < right:
            riskLevel += pos + 1
print(riskLevel)
