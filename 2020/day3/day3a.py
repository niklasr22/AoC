file = open("./2020/day3/input.txt")
data = file.read()

rows = list(filter(lambda x: x != "", data.split("\n")))
w = len(rows[0])
x = 0
y = 0
trees = 0
while y < len(rows):
    if rows[y][x % w] == "#":
        trees += 1
    x += 3
    y += 1

print(trees, "trees")
