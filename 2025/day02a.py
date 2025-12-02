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
        hl = len(si) // 2
        if hl == 0:
            continue
        inv = int(si[:hl] + si[:hl])
        if ia <= inv <= ib:
            invalids.add(inv)


#     hl = len(a) // 2
#     if hl >= 1:
#         inv = int(a[:hl] + a[:hl])
#         if ia <= inv <= ib:
#             invalid_sum += inv
#             print(inv)

#     hl = len(b) // 2
#     if hl >= 1:
#         inv2 = int(b[:hl] + b[:hl])
#         if inv != inv2 and ia <= inv2 <= ib:
#             invalid_sum += inv2
#             print(inv2)
#     print("--")

print(sum(invalids))
