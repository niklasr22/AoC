import itertools
from collections import Counter
from functools import cache
from pathlib import Path

import numpy as np

codes = Path("2024/inputs/day21.txt").read_text().strip().splitlines()

NUM_PAD = np.array([["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"], ["X", "0", "A"]])
DIR_PAD = np.array((["x", "^", "A"], ["<", "v", ">"]))


dir_pad_paths = {
    ("A", ">"): ("v",),
    ("A", "^"): ("<",),
    ("A", "v"): ("<", "v"),
    ("A", "<"): ("v", "<", "<"),
    (">", "A"): ("^",),
    (">", "v"): ("<",),
    (">", "<"): ("<", "<"),
    (">", "^"): ("<", "^"),
    ("^", "A"): (">",),
    ("^", "v"): ("v",),
    ("^", ">"): ("v", ">"),
    ("^", "<"): ("v", "<"),
    ("v", "^"): ("^",),
    ("v", ">"): (">",),
    ("v", "<"): ("<",),
    ("v", "A"): ("^", ">"),
    ("<", "A"): (">", ">", "^"),
    ("<", "v"): (">",),
    ("<", ">"): (">", ">"),
    ("<", "^"): (">", "^"),
}


def _num_move(pos, target, order):
    pos = np.argwhere(NUM_PAD == pos)[0]
    target = np.argwhere(NUM_PAD == target)[0]

    moves = []
    for o in order:
        if o == "<" and target[1] < pos[1]:
            moves.extend(["<"] * (pos[1] - target[1]))
            pos[1] = target[1]
        if o == "v" and target[0] > pos[0]:
            moves.extend(["v"] * (target[0] - pos[0]))
            pos[0] = target[0]
        if o == ">" and target[1] > pos[1]:
            moves.extend([">"] * (target[1] - pos[1]))
            pos[1] = target[1]
        if o == "^" and target[0] < pos[0]:
            moves.extend(["^"] * (pos[0] - target[0]))
            pos[0] = target[0]
        if pos[0] == 3 and pos[1] == 0:
            return None
    # press A
    moves.append("A")
    return tuple(moves)


def find_shortest_for_dir_on_dir(s, t):
    if s == t:
        return ("A",)
    return dir_pad_paths[(s, t)] + ("A",)


def solve_numeric_code(code, order):
    start = "A"
    actions = []
    for c in code:
        res = _num_move(start, c, order)
        if res is None:
            return None
        actions.append(res)
        start = c
    return actions


@cache
def solve_directional_code(code):
    actions = []
    start = "A"
    for c in code:
        b = find_shortest_for_dir_on_dir(start, c)
        if b is None:
            return None
        actions.append(b)
        start = c
    return actions


def solve_code(code, pads=25):
    best = None
    for order0 in itertools.permutations(["<", "v", ">", "^"]):
        last_bot1 = solve_numeric_code(code, order0)
        if not last_bot1:
            continue

        ip = last_bot1
        counter = Counter(ip)
        for _ in range(pads):
            new = Counter()
            for section, count in counter.items():
                b = solve_directional_code(section)
                if b is None:
                    continue
                for s in b:
                    new[s] += count
            counter = new
        l = sum([len(s) * c for s, c in counter.items()])
        if best is None or l < best:
            best = l
    return best


result = 0
for code in codes[:]:
    seq_l = solve_code(code)
    result += seq_l * int(code[:-1])

print(result)
