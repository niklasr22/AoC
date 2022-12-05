import aocutils

lines = aocutils.read_lines("./2022/inputs/day3.txt")


def get_prio(item: str) -> int:
    if ord(item) <= ord("Z"):
        return ord(item) - ord("A") + 27
    return ord(item) - ord("a") + 1


def group(rucksacks: str) -> int:
    for item in rucksacks[0]:
        if item in rucksacks[1] and item in rucksacks[2]:
            return get_prio(item)


priorities = [group(lines[i : i + 3]) for i in range(0, len(lines), 3)]
print(sum(priorities))
