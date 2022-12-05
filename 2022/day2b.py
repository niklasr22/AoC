import aocutils

lines = aocutils.read_lines("./2022/inputs/day2.txt")

# rock = 0, paper = 1, scissors = 2; loss = 0, draw = 1, win = 2
games = [(ord(l[0]) - ord("A"), ord(l[2]) - ord("X")) for l in lines]


def shape(op: int, outcome: int) -> int:
    if outcome == 1:
        return op
    if outcome == 0:
        return (op + 2) % 3
    if outcome == 2:
        return (op + 1) % 3


def score(op: int, me: int) -> int:
    if op == me:
        return 3 + me + 1
    if (me + 2) % 3 == op:
        return 6 + me + 1
    return me + 1


scores = [score(g[0], shape(g[0], g[1])) for g in games]
print(sum(scores))
