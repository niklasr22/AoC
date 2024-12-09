from pathlib import Path

data = list(Path("2024/inputs/day9.txt").read_text().strip())

blocks = [
    (id_ // 2, int(size)) if id_ % 2 == 0 else (None, int(size))
    for id_, size in enumerate(data)
]


def get_next_file(blocks, last_file_i):
    i = last_file_i - 1
    while blocks[i][0] is None:
        i -= 1
    return i


def get_next_gap(blocks, last_gap_i):
    i = last_gap_i + 1
    while blocks[i][0] is not None:
        i += 1
    return i


current_file = get_next_file(blocks, len(blocks))
while current_file >= 0:
    last_id, last_size = blocks[current_file]

    current_gap = get_next_gap(blocks, 0)
    while current_gap < len(blocks):
        _, gap_size = blocks[current_gap]

        if current_gap > current_file:
            break

        if last_size <= gap_size:
            blocks[current_gap] = blocks[current_file]
            blocks[current_file] = (None, last_size)

            if last_size != gap_size:
                blocks.insert(current_gap + 1, (None, gap_size - last_size))
            break

        current_gap = get_next_gap(blocks, current_gap)

    current_file = get_next_file(blocks, current_file)


checksum = pos = 0
for id_, size in blocks:
    if id_ is not None:
        for j in range(size):
            checksum += (pos + j) * id_
    pos += size
print(checksum)
