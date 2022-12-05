import copy

data = open("./2020/day11/input.txt").read()
seats = list(map(lambda row: [c for c in row], data.splitlines()))

h = [0, 1, 1, 1]
v = [1, 0, 1, -1]

height = len(seats)
width = len(seats[0])


def compSeats(seats1, seats2):
    if seats2 == None:
        return False
    for y in range(len(seats1)):
        for x in range(len(seats1[y])):
            if seats1[y][x] != seats2[y][x]:
                return False
    return True


def getOccupiedSeats(x, y, seats):
    n = 0
    for i in range(4):
        for o in range(-1, -width - 1, -1):
            xx = x + h[i] * o
            yy = y + v[i] * o
            if 0 <= xx < width and 0 <= yy < height:
                if seats[yy][xx] == "#":
                    n += 1
                    break
                elif seats[yy][xx] == "L":
                    break
                seats[yy][xx] = "0"
        for o in range(1, width):
            xx = x + h[i] * o
            yy = y + v[i] * o
            if 0 <= xx < width and 0 <= yy < height:
                if seats[yy][xx] == "#":
                    n += 1
                    break
                elif seats[yy][xx] == "L":
                    break
                seats[yy][xx] = "0"
    return n


# print(getOccupiedSeats(9, 0, seats))

# for y in range(height):
#    print("".join(seats[y]))
# exit(0)


def rearrange(seats: list):
    newSeats = copy.deepcopy(seats)
    for y in range(height):
        for x in range(width):
            if seats[y][x] == "L":
                n = getOccupiedSeats(x, y, seats)
                if n == 0:
                    newSeats[y][x] = "#"
            elif seats[y][x] == "#":
                n = getOccupiedSeats(x, y, seats)
                if n >= 5:
                    newSeats[y][x] = "L"
    return newSeats


def printSeats(seats):
    for y in range(height):
        print("".join(seats[y]))
    print()


seatsCopy = None
cnt = 0
while not compSeats(seats, seatsCopy):
    seatsCopy = copy.deepcopy(seats)
    seats = rearrange(seats)
    # printSeats(seats)
    cnt += 1

print("finished", cnt)

count = 0
for y in range(height):
    for x in range(width):
        if seats[y][x] == "#":
            count += 1
print(count)
