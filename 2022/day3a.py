import aocutils

lines = aocutils.read_lines("./2022/inputs/day3.txt")


def get_prio(item: str) -> int:
    if ord(item) <= ord("Z"):
        return ord(item) - ord("A") + 27
    return ord(item) - ord("a") + 1


def search_compartments(rucksack: str):
    first_compartment = rucksack[: len(rucksack) // 2]
    second_compartment = rucksack[len(rucksack) // 2 :]
    for item in first_compartment:
        if item in second_compartment:
            return get_prio(item)


priorities = [search_compartments(l) for l in lines]
print(sum(priorities))
