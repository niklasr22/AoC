import copy

data = open("./2020/day11/input.txt").read()
seats = list(map(lambda row: [c for c in row], data.splitlines()))

h = [-1, -1, -1, 0, 0, 1, 1, 1]
v = [0, -1, 1, -1, 1, 0, -1, 1]


def compSeats(seats1, seats2):
    if seats2 == None:
        return False
    for y in range(len(seats1)):
        for x in range(len(seats1[y])):
            if seats1[y][x] != seats2[y][x]:
                return False
    return True


height = len(seats)
width = len(seats[0])


def rearrange(seats: list):
    newSeats = copy.deepcopy(seats)
    for y in range(height):
        for x in range(width):
            if seats[y][x] == "L":
                a = True
                for i in range(8):
                    xx = x + h[i]
                    yy = y + v[i]
                    if 0 <= xx < width and 0 <= yy < height and seats[yy][xx] == "#":
                        a = False
                if a:
                    newSeats[y][x] = "#"
            elif seats[y][x] == "#":
                n = 0
                for i in range(8):
                    xx = x + h[i]
                    yy = y + v[i]
                    if 0 <= xx < width and 0 <= yy < height and seats[yy][xx] == "#":
                        n += 1
                if n >= 4:
                    newSeats[y][x] = "L"
    return newSeats


seatsCopy = None
cnt = 0
while not compSeats(seats, seatsCopy):
    seatsCopy = copy.deepcopy(seats)
    seats = rearrange(seats)
    # for y in range(height):
    #    print("".join(seats[y]))
    # print()
    cnt += 1

print("finished", cnt)

count = 0
for y in range(height):
    for x in range(width):
        if seats[y][x] == "#":
            count += 1
print(count)
