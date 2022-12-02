import aocutils

lines = aocutils.read_lines("./2022/inputs/day2.txt")
map = {
    "A": 1,
    "B": 2,
    "C": 3,
    "X": 1,
    "Y": 2,
    "Z": 3,
}
games = [(map[l[0]], map[l[2]]) for l in lines]

def shape(op: int, outcome: int) -> int:
    if outcome == 2:
        return op
    if outcome == 1:
        if op == 1:
            return 3
        if op == 2:
            return 1
        if op == 3:
            return 2
    if outcome == 3:
        if op == 1:
            return 2
        if op == 2:
            return 3
        if op == 3:
            return 1

def score(op: int, me: int) -> int:
    if op == me:
        return 3 + me
    if (me == 1 and op == 3) or (me == 2 and op == 1) or (me == 3 and op == 2):
        return 6 + me
    return me

scores = [score(g[0], shape(g[0], g[1])) for g in games]
print(sum(scores))

