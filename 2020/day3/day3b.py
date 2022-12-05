file = open("./2020/day3/input.txt")
data = file.read()

rows = list(filter(lambda x: x != "", data.split("\n")))
w = len(rows[0])


def test(xs, ys):
    global w
    trees = 0
    x = 0
    y = 0
    while y < len(rows):
        if rows[y][x % w] == "#":
            trees += 1
        x += xs
        y += ys
    return trees


trees = 1
trees *= test(1, 1)
trees *= test(3, 1)
trees *= test(5, 1)
trees *= test(7, 1)
trees *= test(1, 2)

print(trees, "trees")
