import re
from functools import cache

import aocutils

MINUTES = 32


def check_plan(plan: tuple, inventory: list) -> bool:
    return (
        plan[0] <= inventory[0] and plan[1] <= inventory[1] and plan[2] <= inventory[2]
    )


@cache
def new_bot(
    bp: tuple,
    minute: int,
    robots: tuple,
    new_inventory: tuple,
    max_bots: tuple,
    bot_i: int,
) -> int:
    new_robots = list(robots)
    new_robots[bot_i] += 1
    new_robots = tuple(new_robots)

    branch_inventory = (
        new_inventory[0] - bp[bot_i][0],
        new_inventory[1] - bp[bot_i][1],
        new_inventory[2] - bp[bot_i][2],
        new_inventory[3],
    )
    return simulate_min(bp, minute + 1, new_robots, branch_inventory, max_bots)


max_geodes_per_minute = list()


@cache
def simulate_min(
    bp: tuple, minute: int, robots: tuple, inventory: tuple, max_bots: tuple
) -> int:
    if minute > MINUTES:
        return inventory[3]

    # collect phase
    new_inventory = (
        inventory[0] + robots[0],
        inventory[1] + robots[1],
        inventory[2] + robots[2],
        inventory[3] + robots[3],
    )

    if max_geodes_per_minute[minute] > new_inventory[3]:
        return 0
    else:
        max_geodes_per_minute[minute] = new_inventory[3]

    if check_plan(bp[3], inventory):
        max_geodes = new_bot(bp, minute, robots, new_inventory, max_bots, 3)
    else:
        max_geodes = 0
        for i in range(4):
            if robots[i] <= max_bots[i] and check_plan(bp[i], inventory):
                max_geodes = max(
                    max_geodes, new_bot(bp, minute, robots, new_inventory, max_bots, i)
                )

        # building nothing
        max_geodes = max(
            max_geodes, simulate_min(bp, minute + 1, robots, new_inventory, max_bots)
        )

    return max_geodes


def max_geode_for_bp(bp) -> int:
    global max_geodes_per_minute
    print("Blueprint", bp)
    max_bots = (max(bp[0][0], bp[1][0], bp[2][0], bp[3][0]), bp[2][1], bp[3][2], 1000)
    max_geodes_per_minute = [0] * (MINUTES + 1)
    simulate_min.cache_clear()
    new_bot.cache_clear()
    g = simulate_min(
        bp=bp, minute=1, robots=(1, 0, 0, 0), inventory=(0, 0, 0, 0), max_bots=max_bots
    )
    print(g)
    return g


blueprints_raw = aocutils.read_lines("./2022/inputs/day19.txt")[:3]
blueprints = dict()
for bp in blueprints_raw:
    numbers = list(map(int, re.findall("[\d]+", bp)))
    blueprints[numbers[0]] = (
        (numbers[1], 0, 0),
        (numbers[2], 0, 0),
        (numbers[3], numbers[4], 0),
        (numbers[5], 0, numbers[6]),
    )

result = 1
for id, bp in blueprints.items():
    result *= max_geode_for_bp(bp)
print(result)
