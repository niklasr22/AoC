from pathlib import Path
import re


instructions = Path("2024/inputs/day3.txt").read_text().strip()

matches = re.findall(r"mul\((\d+),(\d+)\)", instructions)

res = 0
for m in matches:
    res += int(m[0]) * int(m[1])

print(res)
    