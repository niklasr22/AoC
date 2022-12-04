import aocutils

lines = aocutils.read_lines("./2022/inputs/day4.txt")

def prepare_data(pair: str) -> tuple[int,int,int,int]:
    e1r, e2r = pair.split(",", 2)
    e1 = e1r.split("-")
    e2 = e2r.split("-")
    return int(e1[0]), int(e1[1]), int(e2[0]), int(e2[1])

def check_for_complete_overlap(pair: str) -> int:
    e1l, e1u, e2l, e2u = prepare_data(pair)
    if (e1l in range(e2l, e2u + 1) and e1u in range(e2l, e2u + 1)) or (e2l in range(e1l, e1u + 1) and e2u in range(e1l, e1u + 1)):
        return 1
    return 0

def check_for_overlap(pair: str) -> int:
    e1l, e1u, e2l, e2u = prepare_data(pair)
    if e1l in range(e2l, e2u + 1) or e1u in range(e2l, e2u + 1) or e2l in range(e1l, e1u + 1) or e2u in range(e1l, e1u + 1):
        return 1
    return 0

print("a)", sum([check_for_complete_overlap(l) for l in lines]))
print("b)", sum([check_for_overlap(l) for l in lines]))
