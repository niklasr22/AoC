from pathlib import Path

records = [
    (
        line.split(" ")[0],
        list(map(int, line.split(" ")[1].split(","))),
        sum(list(map(int, line.split(" ")[1].split(",")))),
    )
    for line in Path("2023/inputs/day12.txt").read_text().splitlines()
]
# 2333912001156
# 2333912790955
# 2333912790955 tl
# 2541778942849
# 2541781206429 tl
# 2532521202396
# 2532521202396
# 14639333688074 f


def get_groups(record):
    return str([len(g) for g in record.split(".") if len(g) > 0])


def solve(record: str, groups: list, total_functional: int):
    if record.count("#") == total_functional and get_groups(record) == str(groups):
        return 1

    i = record.find("?")
    if i == -1 and get_groups(record) != str(groups):
        return 0

    record_non_functional = record[:i] + "." + record[i + 1 :]
    record_functional = record[:i] + "#" + record[i + 1 :]
    return solve(record_non_functional, groups, total_functional) + solve(
        record_functional, groups, total_functional
    )


arrangements = []
for record in records:
    # if (
    #     record[0].endswith(".")
    #     or record[0].startswith(".")
    #     or record[0].startswith("#")
    #     or (record[0].endswith("?") and record[0].startswith("#"))
    # ):
    #     x = (
    #         solve(record[0], record[1], record[2])
    #         * solve("?" + record[0], record[1], record[2]) ** 4
    #     )
    # else:
    #     x = (
    #         solve(record[0], record[1], record[2])
    #         * solve(record[0] + "?", record[1], record[2]) ** 4
    #     )
    if record[0].endswith("#") and record[0].startswith("?"):
        x = (
            solve(record[0], record[1], record[2])
            * solve(record[0] + "?", record[1], record[2]) ** 4
        )
    else:
        x = (
            (
                solve("?" + record[0], record[1], record[2])
                + solve(record[0] + "?", record[1], record[2])
                - solve(record[0], record[1], record[2])
            )
            ** 4
        ) * solve(record[0], record[1], record[2])
    print(x)
    arrangements.append(x)

print("---")
print(sum(arrangements))
