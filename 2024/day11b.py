from collections import defaultdict
from pathlib import Path

stones = Path("2024/inputs/day11.txt").read_text().strip().split(" ")

cache = defaultdict(dict)


def recurse_blink(history, blinks, target_blinks):
    if blinks == target_blinks:
        return 1

    stone = history[-1]

    remaining_blinks = target_blinks - blinks

    if stone in cache and remaining_blinks in cache[stone]:
        return cache[stone][remaining_blinks]

    newstones = []
    if stone == "0":
        newstones.append("1")
    elif len(stone) % 2 == 0 and len(stone) > 1:
        newstones.append(stone[: len(stone) // 2])
        newstones.append(str(int(stone[len(stone) // 2 :])))
    else:
        newstones.append(str(int(stone) * 2024))

    total = 0
    for newstone in newstones:
        new_history = history + [newstone]
        total += recurse_blink(new_history, blinks + 1, target_blinks)
    cache[stone][remaining_blinks] = total
    return total


total = 0
for stone in stones:
    total += recurse_blink([stone], 0, 75)
print(total)
