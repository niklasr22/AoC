file = open("./2020/day5/input.txt")
data = file.read()

rows = list(data.split("\n"))
def calc(l: int, r: int, c: str):
    if l + 1 == r:
        return int(l)
    if c[0] == "B" or c[0] == "R":
        return calc(l + (r - l) / 2, r, c[1:])
    elif c[0] == "F" or c[0] == "L":
        return calc(l, r - (r - l) / 2, c[1:])
hid = 0
for r in rows:
    rowNr = calc(0, 128, r[:7])
    colNr = calc(0, 8, r[7:])
    id = rowNr * 8 + colNr
    if id > hid:
        hid = id
print(hid)