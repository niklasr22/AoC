import re
from pathlib import Path

input = Path("2023/inputs/day1.txt").read_text()


def get_number(input: str) -> str:
    map = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    digit_str = re.sub(
        r"(?=(" + "|".join(map.keys()) + r"))",
        lambda x: map[x.group(1)],
        input,
    )
    digit_str = re.sub("[a-z]", "", digit_str)

    return int(digit_str[0] + digit_str[-1])


result = sum(get_number(line) for line in input.splitlines())
print(result)
