import math
from pathlib import Path

# (min_steps + 1)
# steps = 50  # 14 * (9 // 2)
steps = 26501365
# steps = 5000

# ms = 14
ms = 131

# pathlength = 20
# steps = 1 + pathlength + steps % pathlength + steps % ms
# steps = 1 + 20 + 10 + 8
# steps = 1 + 131 * 2 + 26501365 % 131 + 26501365 % ms
# 1 + shortest path between starting points of two grid copies * 2 (because of alternating state) + steps % previous + steps % ms

hb = (steps // ms) * 2 - 1


def gauss(n):
    return n * (n + 1) / 2


def calc_cells(w):
    c = int(w**2 - 4 * gauss(math.ceil(w / 2) - 1))
    # no_org_kind = 1 + sum(range(0, (c - 1) // 2 + 1 - 4, 8))
    no_org_kind = 1
    no_other_kind = 0
    a = True
    i = 0
    while no_org_kind + no_other_kind < c:
        i += 4
        if a:
            no_other_kind += i
        else:
            no_org_kind += i
        a = not a

    return c, no_org_kind, c - no_org_kind


# example 50 steps
# total_inner, no_org_kind_inner, no_other_kind_inner = calc_cells(hb)
# print("HB", hb)
# print(total_inner, no_org_kind_inner, no_other_kind_inner)

# print(
#     no_org_kind_inner * 42 + no_other_kind_inner * 39,
#     no_org_kind_inner * 42
#     + no_other_kind_inner * 39
#     + (17 + 15 + 18 + 15)
#     + (6 + 9 + 2 + 9)
#     + (6 + 36) * (hb // 2)
#     + (9 + 38) * (hb // 2)
#     + (2 + 29) * (hb // 2)
#     + (9 + 38) * (hb // 2),
# )


# total_inner, no_org_kind_inner, no_other_kind_inner = calc_cells(hb)
# print("HB", hb)
# print(total_inner, no_org_kind_inner, no_other_kind_inner)

# print(
#     no_org_kind_inner * 7520 + no_other_kind_inner * 7457,
#     no_org_kind_inner * 7520
#     + no_other_kind_inner * 7457
#     + (3049 + 3046 + 3052 + 3040)  # top + left + right + bottom
#     + (96 + 100 + 97 + 98)  # otl + obl + otr+ obr
#     + (96 + 4805) * (hb // 2)  # (otl + otli) * (hb//2)
#     + (100 + 4822) * (hb // 2)  # (obl + obli) * (hb//2)
#     + (97 + 4827) * (hb // 2)  # (otr + otri) * (hb//2)
#     + (98 + 4812) * (hb // 2),  # (obr + obri) * (hb//2)
# )


# bv = {
#     "Top": 17,
#     "Bottom": 15,
#     "Left": 18,
#     "Right": 15,
#     "OTL": 6,
#     "OTLI": 36,
#     "OBL": 9,
#     "OBLI": 38,
#     "OTR": 9,
#     "OTRI": 38,
#     "OBR": 2,
#     "OBRI": 29,
#     "CENTER": 39,
#     "ALTERNATE": 42,
# }

# total_inner, no_org_kind_inner, no_other_kind_inner = calc_cells(hb)
# print("HB", hb)
# print(total_inner, no_org_kind_inner, no_other_kind_inner)

# print(
#     no_org_kind_inner * bv["ALTERNATE"]
#     + no_other_kind_inner * bv["CENTER"]
#     + (
#         bv["Top"] + bv["Bottom"] + bv["Left"] + bv["Right"]
#     )  # top + left + right + bottom
#     + (bv["OTL"] + bv["OBL"] + bv["OTR"] + bv["OBR"])  # otl + obl + otr+ obr
#     + (bv["OTL"] + bv["OTLI"]) * (hb // 2)  # (otl + otli) * (hb//2)
#     + (bv["OBL"] + bv["OBLI"]) * (hb // 2)  # (obl + obli) * (hb//2)
#     + (bv["OTR"] + bv["OTRI"]) * (hb // 2)  # (otr + otri) * (hb//2)
#     + (bv["OBR"] + bv["OBRI"]) * (hb // 2),  # (obr + obri) * (hb//2)
# )


total_inner, no_org_kind_inner, no_other_kind_inner = calc_cells(hb)
print("HB", hb)
print(total_inner, no_org_kind_inner, no_other_kind_inner)

# print(
#     no_org_kind_inner * 7457 + no_other_kind_inner * 7520,
#     no_org_kind_inner * 7457
#     + no_other_kind_inner * 7520
#     + (3049 + 3046 + 3052 + 3040)  # top + left + right + bottom
#     + (96 + 100 + 97 + 98)  # otl + obl + otr+ obr
#     + (96 + 4805) * (hb // 2)  # (otl + otli) * (hb//2)
#     + (100 + 4822) * (hb // 2)  # (obl + obli) * (hb//2)
#     + (97 + 4827) * (hb // 2)  # (otr + otri) * (hb//2)
#     + (98 + 4812) * (hb // 2),  # (obr + obri) * (hb//2)
# )

print(
    no_org_kind_inner * 7457 + no_other_kind_inner * 7520,
    no_org_kind_inner * 7520
    + no_other_kind_inner * 7457
    + (5678 + 5674 + 5678 + 5674)  # top + left + right + bottom
    + (950) * (hb // 2 + 1)  # (otl + otli) * (hb//2)
    + (943) * (hb // 2 + 1)  # (obl + obli) * (hb//2)
    + (948) * (hb // 2 + 1)  # (otr + otri) * (hb//2)
    + (965) * (hb // 2 + 1)  # (obr + obri) * (hb//2)
    + (6587) * (hb // 2)  # (otl + otli) * (hb//2)
    + (6611) * (hb // 2)  # (obl + obli) * (hb//2)
    + (6587) * (hb // 2)  # (otr + otri) * (hb//2)
    + (6607) * (hb // 2),  # (obr + obri) * (hb//2)
)

# 612941160286969 f
# 612941134797232 wooooohooooo

# 622406329597945 f
# 622406303912152 f
# 622407147878726 f
# 622407173564519 f
# 622407173564519 f

# 622404172594133 f
# 622404180748458 f

# 622406254174913 f
# 622406279860832 too high
# 622410287070802 too high


# example 100 steps
# total_inner, no_org_kind_inner, no_other_kind_inner = calc_cells(hb)
# print("HB", hb)
# print(total_inner, no_org_kind_inner, no_other_kind_inner)

# print(
#     no_org_kind_inner * 42 + no_other_kind_inner * 39,
#     no_org_kind_inner * 42
#     + no_other_kind_inner * 39
#     + (4 + 39 + 35 + 2 + 4 + 35 + 33 + 1 + 1)
#     + 1 * (hb // 2)  # b
#     + 1 * (hb // 2)  # n
#     + 1 * (hb // 2)  # d
#     + 0 * (hb // 2)  # a
#     + 21 * (hb // 2 - 1)  # e
#     + 25 * (hb // 2 - 1)  # g
#     + 12 * (hb // 2 - 1)  # q
#     + 21 * (hb // 2 - 1)  # o
#     + 41 * (hb // 2 - 2)  # p
#     + 42 * (hb // 2 - 2) * 3,  # h
# )

# BEHIHIHGD
