from os import pipe


data = open("./2020/day13/input.txt").read()
data = data.splitlines()

earliest = int(data[0])
busses = list(map(int, filter(lambda x : x != 'x', data[1].split(","))))

options = {}
for b in busses:
    m = earliest // b
    w = b * (m + 1) - earliest
    print(b, w, earliest, b * (m + 1))
    options[w] = b

bus = min(options.keys())
print(options[bus] * bus)