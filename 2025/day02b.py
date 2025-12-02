from pathlib import Path

data = Path("2025/inputs/day02.txt").read_text().strip().split(",")


def parse(r):
    a, b = r.split("-")
    return a, b, int(a), int(b)


ids = list(map(parse, data))

invalids = set()

for a, b, ia, ib in ids:
    for i in range(ia, ib + 1):
        si = str(i)
        for l in range(1, len(si) // 2 + 1):
            f = len(si) // l
            if l * f != len(si):
                continue
            inv = int(si[:l] * f)
            if ia <= inv <= ib:
                invalids.add(inv)

print(sum(invalids))
