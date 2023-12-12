from functools import cache
from pathlib import Path


def get_groups(record):
    return tuple(
        [g.count("#") for g in record.replace("?", ".").split(".") if len(g) > 0]
    )


def list_smaller(a, b):
    return all(a[i] >= b[i] for i in range(min(len(a), len(b))))


def list_eq_last_leq(a, b):
    if len(b) == 0:
        return True
    ub = min(len(a) - 1, len(b) - 1)
    return all(a[i] == b[i] for i in range(ub)) and a[ub] >= b[ub]


def list_sw(a, b):
    return a[: len(b)] == b


@cache
def solve(record: str, groups: tuple):
    current_groups = get_groups(record)

    if record.count("#") > 0 and sum(groups) == 0:
        return 0

    if record.count("#") == sum(groups) and current_groups == groups:
        return 1

    i = record.find("?")
    if i == -1 and current_groups != groups:
        return 0

    finished_groups = get_groups(record[:i])
    if not list_eq_last_leq(groups, finished_groups) or len(finished_groups) > len(
        groups
    ):
        return 0

    last_group_end = record.rfind(".", 0, record.find("?"))
    if 0 <= last_group_end:
        previous_groups = get_groups(record[: last_group_end + 1])
        if not list_sw(groups, previous_groups):
            return 0

        if list_sw(groups, previous_groups):
            x = solve(
                record[last_group_end + 1 :],
                groups[len(previous_groups) :],
            )
            return x

    record_non_functional = record[:i] + "." + record[i + 1 :]
    record_functional = record[:i] + "#" + record[i + 1 :]

    return solve(record_non_functional, groups) + solve(record_functional, groups)


def solve_for_input(records: list):
    arrangements = []
    for record in records:
        arrangements.append(solve(record[0], record[1]))

    return sum(arrangements)


records = [
    (
        line.split(" ")[0],
        tuple(map(int, line.split(" ")[1].split(","))),
    )
    for line in Path("2023/inputs/day12.txt").read_text().splitlines()
]
print("a:", solve_for_input(records))

records = [
    (
        "?".join([line.split(" ")[0]] * 5),
        tuple(map(int, line.split(" ")[1].split(","))) * 5,
    )
    for line in Path("2023/inputs/day12.txt").read_text().splitlines()
]
print("b:", solve_for_input(records))
