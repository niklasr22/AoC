import re
from pathlib import Path

input = Path("2023/inputs/day1.txt").read_text()


def get_number(input: str) -> str:
    map = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    forward = input
    found = False
    i = 0
    while i < len(forward) and not found:
        prefix = forward[:i]
        part = forward[i:]
        for word, digit in map.items():
            if part.startswith(word):
                forward = prefix + str(digit) + part[len(word) :]
                found = True
                break
        i += 1

    backward = input
    found = False
    i = len(backward)
    while i >= 0 and not found:
        suffix = backward[i:]
        part = backward[:i]
        for word, digit in map.items():
            if part.endswith(word):
                backward = part[: -len(word)] + str(digit) + suffix
                found = True
                break
        i -= 1

    forward = re.sub("[a-z]", "", forward)
    backward = re.sub("[a-z]", "", backward)

    return int(forward[0] + backward[-1])


numbers = [get_number(line) for line in input.splitlines()]
result = sum(numbers)

print(result)
