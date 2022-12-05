from functools import lru_cache
from typing import Tuple

cavesA = (("B", "C"), ("A", "D"), ("D", "A"), ("C", "B"))
cavesB = (
    ("B", "D", "D", "C"),
    ("A", "B", "C", "D"),
    ("D", "A", "B", "A"),
    ("C", "C", "A", "B"),
)
hallway = ("",) * 11
cavepositions = [2, 4, 6, 8]


def reachedTarget(caves):
    for i in range(len(caves)):
        w = getWished(i)
        for a in caves[i]:
            if a != w:
                return False
    return True


def getCave(caves: Tuple, c):
    if c == 2:
        return caves[0]
    if c == 4:
        return caves[1]
    if c == 6:
        return caves[2]
    if c == 8:
        return caves[3]


def getDestination(c):
    if c == "A":
        return 2
    if c == "B":
        return 4
    if c == "C":
        return 6
    if c == "D":
        return 8


def getCosts(c):
    if c == "A":
        return 1
    if c == "B":
        return 10
    if c == "C":
        return 100
    if c == "D":
        return 1000


def getWished(c):
    if c == 0:
        return "A"
    if c == 1:
        return "B"
    if c == 2:
        return "C"
    if c == 3:
        return "D"


@lru_cache(maxsize=None)
def move(caves: Tuple, hallway: Tuple):
    if reachedTarget(caves):
        return 0
    lowestCosts = float("inf")
    # move from hallway to cave
    for pos, hp in enumerate(hallway):
        if hp == "":
            continue
        # try to move to destination
        dest = getDestination(hp)
        # check if hallway is clear:
        clear = True
        for x in range(min(dest, pos), max(dest, pos)):
            if x != pos and hallway[x] != "":
                clear = False
                break
        if not clear:
            continue
        # check cave for other species
        cave = getCave(caves, dest)
        for x in cave:
            if x != hp and x != "":
                clear = False
                break
        if not clear:
            continue

        # move to lowest possible position in cave
        steps = abs(pos - dest)
        caveSteps = 0
        for cp in reversed(cave):
            if cp == "":
                caveSteps += 1
        steps += caveSteps
        movecosts = steps * getCosts(hp)

        newhallway = list(hallway)
        newhallway[pos] = ""
        newhallway = tuple(newhallway)
        newcave = list(cave)
        newcave[len(newcave) - caveSteps] = hp
        newcaves = list(caves)
        newcaves[dest // 2 - 1] = tuple(newcave)
        newcaves = tuple(newcaves)

        costs = movecosts + move(newcaves, newhallway)
        if lowestCosts > costs:
            lowestCosts = costs

    # move from cave to hallway
    for pos, c in enumerate(caves):
        moveHighestOut = False
        wished = getWished(pos)
        for i in c:
            if i == "":
                break
            if i != wished:
                moveHighestOut = True
                break
        if not moveHighestOut:
            continue

        # get amphipod which should be moved
        cp, ct = -1, ""
        for p, i in enumerate(reversed(c)):
            if i != "":
                cp = p
                ct = i
                break
        # cave empty
        if cp == -1:
            continue
        cp = len(c) - cp - 1

        steps = len(c) - cp

        # get any possible hallway spot
        cavepos = getDestination(getWished(pos))
        positions = []
        for i in range(cavepos, -1, -1):
            if not i in cavepositions and hallway[i] == "":
                positions.append(i)
            elif not i in cavepositions and hallway[i] != "":
                break
        for i in range(cavepos, 11):
            if not i in cavepositions and hallway[i] == "":
                positions.append(i)
            elif not i in cavepositions and hallway[i] != "":
                break

        # try possible hallway spots
        for hap in positions:
            movecosts = (steps + abs(hap - cavepos)) * getCosts(ct)

            newhallway = list(hallway)
            newhallway[hap] = ct
            newhallway = tuple(newhallway)
            newcave = list(c)
            newcave[cp] = ""
            newcaves = list(caves)
            newcaves[pos] = tuple(newcave)
            newcaves = tuple(newcaves)

            costs = movecosts + move(newcaves, newhallway)
            if lowestCosts > costs:
                lowestCosts = costs
    return lowestCosts


print("A", move(cavesA, hallway))
print("B", move(cavesB, hallway))
