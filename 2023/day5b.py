import time
from pathlib import Path

start_time = time.time()

almanac = Path("2023/inputs/day5.txt").read_text()

seeds = list(map(int, almanac.splitlines()[0].split(": ")[1].split(" ")))


def parse_map(map_line) -> tuple[int, int, int]:
    return list(map(int, map_line.split(" ")))


def parse_section(section) -> list[tuple[int, int, int]]:
    return [parse_map(line) for line in section.splitlines()[1:]]


def map_io(input_range, mapper):
    ranges_to_be_mapped = [input_range]
    outputs = []
    while ranges_to_be_mapped:
        input_range = ranges_to_be_mapped[0]
        mapped = False
        for dest_range, input_range_start, length in mapper:
            if (
                input_range_start + length - 1 >= input_range[0]
                and input_range[0] + input_range[1] - 1 >= input_range_start
            ):
                min_start = min(input_range[0], input_range_start)
                max_end = max(
                    input_range[0] + input_range[1], input_range_start + length
                )
                overlap_start = max(input_range[0], input_range_start)
                overlap_end = min(
                    input_range[0] + input_range[1], input_range_start + length
                )
                ranges_to_be_mapped.pop(0)
                outputs.append(
                    (
                        dest_range + overlap_start - input_range_start,
                        overlap_end - overlap_start,
                    )
                )
                mapped = True
                if overlap_end - overlap_start < input_range[1]:
                    if min_start != overlap_start and input_range[0] < overlap_start:
                        ranges_to_be_mapped.append(
                            (min_start, overlap_start - min_start)
                        )
                    if (
                        max_end != overlap_end
                        and input_range[0] + input_range[1] > overlap_end
                    ):
                        ranges_to_be_mapped.append(
                            (overlap_end, max_end - overlap_end + 1)
                        )
                break
        if mapped:
            continue

        outputs.append(input_range)
        ranges_to_be_mapped.pop(0)

    return outputs


def seed_to_loc(seed_range, mappers):
    value_ranges = [seed_range]
    for i, mapper in enumerate(mappers):
        new_ranges = []
        for range in value_ranges:
            new_ranges.extend(map_io(range, mapper))
        value_ranges = new_ranges
    return value_ranges


sections = almanac.split("\n\n")
mappers = [parse_section(section) for section in sections[1:]]

min_loc = None
for i in range(0, len(seeds), 2):
    locs = seed_to_loc((seeds[i], seeds[i + 1]), mappers)

    seed_min_loc = min(locs, key=lambda x: x[0])[0]
    if min_loc is None or seed_min_loc < min_loc:
        min_loc = seed_min_loc

print(min_loc)
