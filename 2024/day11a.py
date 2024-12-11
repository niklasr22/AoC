from pathlib import Path

stones = Path("2024/inputs/day11.txt").read_text().strip().split(" ")


def timestep(stones):
    newstones = []

    for stone in stones:
        if stone == "0":
            newstones.append("1")
        elif len(stone) % 2 == 0 and len(stone) > 1:
            newstones.append(stone[: len(stone) // 2])
            newstones.append(str(int(stone[len(stone) // 2 :])))
        else:
            newstones.append(str(int(stone) * 2024))
    return newstones


for blink in range(25):
    stones = timestep(stones)

print(len(stones))
