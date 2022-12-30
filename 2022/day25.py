import aocutils
import math

numbers = aocutils.read_lines("./2022/inputs/day25.txt")


def snafu_to_dec(snafu) -> int:
    result = 0
    for p, d in enumerate(reversed(snafu)):
        match (d):
            case "1" | "2" | "0":
                d = int(d)
            case "-":
                d = -1
            case "=":
                d = -2
        result += d * (5**p)
    return result


def to_snafu_digit(d: int) -> str:
    match (d):
        case 1 | 2 | 0:
            return str(d)
        case -1:
            return "-"
        case -2:
            return "="
    return ""


def dec_to_snafu(dec: int) -> str:
    if dec == 0:
        return "0"
    result = ""
    pot = round(math.log(dec, 5))
    for p in range(pot, -1, -1):
        a = round(dec / (5**p))
        result += to_snafu_digit(a)
        dec -= a * (5**p)
        if dec == 0:
            result += "0" * (p)
            break

    return result


result = 0
for n in numbers:
    result += snafu_to_dec(n)

print(dec_to_snafu(result))
