from collections import defaultdict
from pathlib import Path

stones = Path("2024/inputs/day11.txt").read_text().strip().split(" ")

counter = {s: stones.count(s) for s in set(stones)}
for blink in range(75):
    new_counter = defaultdict(int)
    for stone, count in counter.items():
        if stone == "0":
            new_counter["1"] += count
        elif len(stone) % 2 == 0 and len(stone) > 1:
            new_counter[stone[: len(stone) // 2]] += count
            new_counter[str(int(stone[len(stone) // 2 :]))] += count
        else:
            new_counter[str(int(stone) * 2024)] += count
    counter = new_counter

print(sum(counter.values()))
