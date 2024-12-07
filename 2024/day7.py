from pathlib import Path

lines = Path("2024/inputs/day7.txt").read_text().strip().splitlines()

equations = [
    (int(line.split(": ")[0]), list(map(int, line.split(": ")[1].split(" "))))
    for line in lines
]


def solve(res, remaining_parts, b=False):
    if len(remaining_parts) == 1:
        return res == remaining_parts[0]

    if res < remaining_parts[0]:
        return False

    if solve(res, [remaining_parts[0] + remaining_parts[1]] + remaining_parts[2:], b):
        return True

    if solve(res, [remaining_parts[0] * remaining_parts[1]] + remaining_parts[2:], b):
        return True

    if b:
        combined = int(f"{remaining_parts[0]}{remaining_parts[1]}")
        if res < combined:
            return False
        if solve(res, [combined] + remaining_parts[2:], b):
            return True
    return False


res_a = 0
res_b = 0
for res, parts in equations:
    if solve(res, parts):
        res_a += res
    if solve(res, parts, b=True):
        res_b += res

print("A:", res_a)
print("B:", res_b)
