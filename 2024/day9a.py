from pathlib import Path

data = list(Path("2024/inputs/day9.txt").read_text().strip())

blocks = [
    (id_ // 2, int(size)) if id_ % 2 == 0 else (None, int(size))
    for id_, size in enumerate(data)
]


def get_last_file(blocks):
    for i, (id_, _) in enumerate(reversed(blocks)):
        if id_ is not None:
            return len(blocks) - i - 1
    return -1


def get_first_gap(blocks):
    for i, (id_, _) in enumerate(blocks):
        if id_ is None:
            return i
    return -1


current_gap = 1
current_file = len(blocks)
while current_file > current_gap:
    current_file = get_last_file(blocks)
    if current_file == -1 or current_file < current_gap:
        break
    id_, size = blocks[current_gap]
    if id_ is None:
        last_id, last_size = blocks.pop(current_file)

        if last_size <= size:
            blocks[current_gap] = (last_id, last_size)
            if last_size != size:
                blocks.insert(current_gap + 1, (None, size - last_size))
        else:
            blocks.append((last_id, last_size - size))
            blocks[current_gap] = (last_id, size)

    current_gap = get_first_gap(blocks)

checksum = pos = 0
for id_, size in blocks:
    if id_ is not None:
        for j in range(size):
            checksum += (pos + j) * id_
    pos += size
print(checksum)
