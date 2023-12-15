import re
from collections import defaultdict
from pathlib import Path

text = Path("2023/inputs/day15.txt").read_text().split(",")


def hash(data: str):
    val = 0
    for c in data:
        val += ord(c)
        val = (val * 17) % 256
    return val


boxes = defaultdict(list)
for string in text:
    label, operation, lens = re.split("([=\-])", string)
    box = hash(label)
    if operation == "-":
        boxes[box] = [b_lens for b_lens in boxes[box] if b_lens[0] != label]
    elif operation == "=":
        comp = [b_lens[0] == label for b_lens in boxes[box]]
        if any(comp):
            boxes[box][comp.index(True)] = (label, int(lens))
        else:
            boxes[box].append((label, int(lens)))

# calculate focusing power
power = 0
for box, lenses in boxes.items():
    for i, (label, focal_length) in enumerate(lenses):
        power += (box + 1) * (i + 1) * focal_length

print(power)
