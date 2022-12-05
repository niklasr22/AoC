data = open("./2021/day3/input.txt").read()
rows = data.splitlines()
ones = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
d = 0
oxygen = rows.copy()
co2 = rows.copy()


def filterBy(column, criteria, data):
    if column >= 12:
        return -1
    ones = 0
    for r in data:
        if r[column] == "1":
            ones += 1
    f = "0"
    if criteria == 1:
        f = "1" if len(data) - ones <= ones else "0"
    else:
        f = "0" if len(data) - ones <= ones else "1"
    data = list(filter(lambda x: x[column] == f, data))
    if len(data) != 1:
        return filterBy(column + 1, criteria, data)
    else:
        return data[0]


oxygenRating = int(filterBy(0, 1, oxygen), base=2)
co2Rating = int(filterBy(0, 0, co2), base=2)

print("Oxygen:", oxygenRating)
print("CO2:", co2Rating)
print("Mult:", oxygenRating * co2Rating)
