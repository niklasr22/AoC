import math
import re
from pathlib import Path

ip = re.sub(" +", "", Path("2023/inputs/day6.txt").read_text()).splitlines()


time = int(ip[0].split(":")[1])
distance = int(ip[1].split(":")[1])


c = time
r = distance
min_time = math.ceil((c - (c**2 - 4 * r) ** 0.5) / 2 + 0.00001)
max_time = math.floor((c + (c**2 - 4 * r) ** 0.5) / 2 - 0.00001)

print(max_time - min_time + 1)
