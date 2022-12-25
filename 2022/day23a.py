from collections import defaultdict

import aocutils

map = aocutils.read_lines("./2022/inputs/day23.txt", lambda x: list(x))

elves = dict()
i = 0
for y, row in enumerate(map):
    for x, col in enumerate(row):
        if col == "#":
            elves[i] = (x, y)
            i += 1

adjacents = {
    "N": (0, -1),
    "NE": (1, -1),
    "E": (1, 0),
    "SE": (1, 1),
    "S": (0, 1),
    "SW": (-1, 1),
    "W": (-1, 0),
    "NW": (-1, -1),
}

considerations = [
    ("N", "NE", "NW"),
    ("S", "SE", "SW"),
    ("W", "NW", "SW"),
    ("E", "NE", "SE"),
]
first_consideration = 0


def all_adjacents_clear(elve: int) -> bool:
    e_x, e_y = elves[elve]
    for (x, y) in adjacents.values():
        if (e_x + x, e_y + y) in elves.values():
            return False
    return True


def some_adjacents_clear(elve: int, directions: tuple) -> bool:
    e_x, e_y = elves[elve]
    for d in directions:
        x, y = adjacents[d]
        if (e_x + x, e_y + y) in elves.values():
            return False
    return True


def print_map():
    elves_x = list(e[0] for e in elves.values())
    elves_y = list(e[1] for e in elves.values())
    area = (max(elves_x) - min(elves_x)) * (max(elves_y) - min(elves_y))
    for y in range(min(elves_y), max(elves_y) + 1):
        line = ""
        for x in range(min(elves_x), max(elves_x) + 1):
            if (x, y) in elves.values():
                line += "#"
            else:
                line += "."
        print(line)
    print()
    print()


# simulation
def round(first_consideration) -> None:
    # first half
    proposals = dict()
    proposal_count = defaultdict(lambda: 0)
    for e in elves:
        if all_adjacents_clear(e):
            continue
        for i in range(4):
            directions = considerations[(first_consideration + i) % 4]
            if some_adjacents_clear(e, directions):
                x, y = adjacents[directions[0]]
                e_x, e_y = elves[e]
                n_x = e_x + x
                n_y = e_y + y
                proposals[e] = (n_x, n_y)
                proposal_count[(n_x, n_y)] += 1
                break

    # second half
    for e, p in proposals.items():
        if proposal_count[p] > 1:
            continue
        elves[e] = p

    # print_map()


# print_map()
for _ in range(10):
    round(first_consideration)
    first_consideration = (first_consideration + 1) % 4

elves_x = list(e[0] for e in elves.values())
elves_y = list(e[1] for e in elves.values())
area = (max(elves_x) - min(elves_x) + 1) * (max(elves_y) - min(elves_y) + 1)
area -= len(elves)
print(area)
