from pathlib import Path

text = Path("2023/inputs/day15.txt").read_text().split(",")


def hash(data: str):
    val = 0
    for c in data:
        val += ord(c)
        val = (val * 17) % 256
    return val


print(sum(hash(string) for string in text))
