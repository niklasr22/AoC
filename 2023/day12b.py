from pathlib import Path

records = [
    (
        "?".join([line.split(" ")[0]] * 5),
        list(map(int, line.split(" ")[1].split(","))) * 5,
        sum(list(map(int, line.split(" ")[1].split(",")))) * 5,
    )
    for line in Path("2023/inputs/day12_sm.txt").read_text().splitlines()
]

records = [
    (
        line.split(" ")[0],
        list(map(int, line.split(" ")[1].split(","))),
        sum(list(map(int, line.split(" ")[1].split(",")))),
    )
    for line in Path("2023/inputs/day12_sm.txt").read_text().splitlines()
]


def get_groups(record):
    return [len(g) for g in record.split(".") if len(g) > 0]


def solve(record: str, groups: list, total_functional: int):
    solved_groups = get_groups(record)
    solved_record = record[: record.find("?")]
    if 0 <= solved_record.rfind("#."):
        partial_groups = str(get_groups(solved_record))[:-1]
        print(partial_groups)
        if not str(groups).startswith(partial_groups):
            return 0

    if record.count("#") == total_functional and str(solved_groups) == str(groups):
        return 1

    i = record.find("?")
    if i == -1 and str(solved_groups) != str(groups):
        return 0

    record_non_functional = record[:i] + "." + record[i + 1 :]
    record_functional = record[:i] + "#" + record[i + 1 :]
    return solve(record_non_functional, groups, total_functional) + solve(
        record_functional, groups, total_functional
    )


arrangements = []
for record in records:
    arrangements.append(solve(record[0], record[1], record[2]))

print(sum(arrangements))
