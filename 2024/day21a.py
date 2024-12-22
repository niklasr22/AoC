import itertools
from pathlib import Path

import numpy as np

codes = Path("2024/inputs/day21.txt").read_text().strip().splitlines()

NUM_PAD = np.array([[7, 8, 9], [4, 5, 6], [1, 2, 3], [-100, 0, 10]])
DIR_PAD = np.array((["x", "^", "A"], ["<", "v", ">"]))


def solve_numeric_code(code, order):
    actions = []
    pos = np.argwhere(NUM_PAD == 10)[0]
    for c in code:
        if c == "A":
            target = np.argwhere(NUM_PAD == 10)[0]
        else:
            target = np.argwhere(NUM_PAD == int(c))[0]

        for o in order:
            if o == "<" and target[1] < pos[1]:
                actions.extend(["<"] * (pos[1] - target[1]))
                pos[1] = target[1]
            if o == "v" and target[0] > pos[0]:
                actions.extend(["v"] * (target[0] - pos[0]))
                pos[0] = target[0]
            if o == ">" and target[1] > pos[1]:
                actions.extend([">"] * (target[1] - pos[1]))
                pos[1] = target[1]
            if o == "^" and target[0] < pos[0]:
                actions.extend(["^"] * (pos[0] - target[0]))
                pos[0] = target[0]
            if pos[0] == 3 and pos[1] == 0:
                return None

        # press A
        actions.append("A")
        pos = target

    return actions


def solve_directional_code(code, order):
    actions = []
    pos = np.argwhere(DIR_PAD == "A")[0]
    for c in code:
        target = np.argwhere(DIR_PAD == c)[0]

        for o in order:
            if o == "<" and target[1] < pos[1]:
                actions.extend(["<"] * (pos[1] - target[1]))
                pos[1] = target[1]
            if o == "v" and target[0] > pos[0]:
                actions.extend(["v"] * (target[0] - pos[0]))
                pos[0] = target[0]
            if o == ">" and target[1] > pos[1]:
                actions.extend([">"] * (target[1] - pos[1]))
                pos[1] = target[1]
            if o == "^" and target[0] < pos[0]:
                actions.extend(["^"] * (pos[0] - target[0]))
                pos[0] = target[0]
            if pos[0] == 0 and pos[1] == 0:
                return None
        # press A
        actions.append("A")
        pos = target

    return actions


def solve_code(code):
    best = None
    for order0 in itertools.permutations(["<", "v", ">", "^"]):
        last_bot1 = solve_numeric_code(code, order0)
        if last_bot1 is None:
            continue

        for order1 in itertools.permutations(["<", "v", ">", "^"]):
            bot2 = solve_directional_code(last_bot1, order1)
            if bot2 is None:
                continue
            for order2 in itertools.permutations(["<", "v", ">", "^"]):
                bot3 = solve_directional_code(bot2, order2)
                if bot3 is None:
                    continue

                if best is None or len(bot3) < len(best):
                    best = bot3
    return best


result = 0
for code in codes[:]:
    seq = solve_code(code)
    result += len(seq) * int(code[:-1])

print(result)
