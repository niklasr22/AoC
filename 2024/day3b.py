from pathlib import Path
import re


instructions = Path("2024/inputs/day3.txt").read_text().strip()

matches = re.findall(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))", instructions)

res = 0
enabled = True
for m in matches:
    if m[2] == "do()":
        enabled = True
    elif m[3] == "don't()":
        enabled = False
    elif enabled:
        res += int(m[0]) * int(m[1])

print(res)
    