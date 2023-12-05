from pathlib import Path

almanac = Path("2023/inputs/day5.txt").read_text()

seeds = list(map(int, almanac.splitlines()[0].split(": ")[1].split(" ")))


def parse_map(map_line) -> tuple[int, int, int]:
    return tuple(map(int, map_line.split(" ")))


def parse_section(section) -> list[tuple[int, int, int]]:
    return [parse_map(line) for line in section.splitlines()[1:]]


def map_io(input, mapper):
    for dest_range, input_range_start, length in mapper:
        if input in range(input_range_start, input_range_start + length):
            return dest_range + input - input_range_start
    return input


def seed_to_loc(seed, mappers):
    val = seed
    for mapper in mappers:
        val = map_io(val, mapper)
        print(val)
    print("-----")
    return val


sections = almanac.split("\n\n")
mappers = [parse_section(section) for section in sections[1:]]

locs = [seed_to_loc(seed, mappers) for seed in seeds]
print(locs)
print(min(locs))
