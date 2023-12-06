import math
import re
from pathlib import Path

ip = re.sub(" +", " ", Path("2023/inputs/day6.txt").read_text()).splitlines()


times = list(map(int, ip[0].split(": ")[1].split(" ")))
distances = list(map(int, ip[1].split(": ")[1].split(" ")))


result = 1
for i in range(len(times)):
    c = times[i]
    r = distances[i]
    min_time = math.ceil((c - (c**2 - 4 * r) ** 0.5) / 2 + 0.00001)
    max_time = math.floor((c + (c**2 - 4 * r) ** 0.5) / 2 - 0.00001)

    result *= max_time - min_time + 1

print(result)
