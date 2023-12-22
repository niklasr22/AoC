from collections import defaultdict
from pathlib import Path

snapshot = Path("2023/inputs/day22.txt").read_text().splitlines()


block_ids = ord("A") - 1


def parse_block(block):
    global block_ids
    xyz1, xyz2 = block.split("~")
    x1, y1, z1 = tuple(map(int, xyz1.split(",")))
    x2, y2, z2 = tuple(map(int, xyz2.split(",")))

    block_ids += 1
    return ((x1, y1, z1), (x2, y2, z2), chr(block_ids))


blocks = list(map(parse_block, snapshot))

blocks.sort(key=lambda b: b[0][2])

settled = []

graph = defaultdict(list)
supported_by_graph = defaultdict(list)


def is_on(block_falling, settled_block):
    bf_x1, bf_x2 = block_falling[0][0], block_falling[1][0]
    bf_y1, bf_y2 = block_falling[0][1], block_falling[1][1]
    bf_lz = block_falling[0][2]

    sb_x1, sb_x2 = settled_block[0][0], settled_block[1][0]
    sb_y1, sb_y2 = settled_block[0][1], settled_block[1][1]
    sb_uz = settled_block[1][2]

    if bf_lz <= sb_uz:
        return False, -1

    if sb_x1 <= bf_x2 and bf_x1 <= sb_x2:
        if bf_y1 <= sb_y2 and sb_y1 <= bf_y2:
            return True, sb_uz + 1
    return False, -1


for block in blocks:
    is_settled = False

    # check highest ending block first
    for settled_block in reversed(settled):
        lays_on, new_lz = is_on(block, settled_block)
        if lays_on:
            if is_settled and block[0][2] != new_lz:
                continue

            # update z coordinates of block
            (x1, y1, z1), (x2, y2, z2), block_id = block
            block = ((x1, y1, new_lz), (x2, y2, new_lz + z2 - z1), block_id)

            graph[settled_block].append(block)
            supported_by_graph[block].append(settled_block)

            if not is_settled:
                settled.append(block)
            is_settled = True

    if not is_settled:
        # put block on the ground
        (x1, y1, z1), (x2, y2, z2), block_id = block
        block = ((x1, y1, 1), (x2, y2, 1 + z2 - z1), block_id)
        settled.append(block)

    settled.sort(key=lambda b: b[1][2])

disintegration_blocks = set()
for block, supported_by in supported_by_graph.items():
    for support in supported_by:
        needed = False
        for supported_by_support in graph[support]:
            if len(supported_by_graph[supported_by_support]) == 1:
                needed = True
                break
        if not needed:
            disintegration_blocks.add(support[2])


for block in settled:
    # add blocks that don't support any other blocks
    if len(graph[block]) == 0:
        disintegration_blocks.add(block[2])

print(len(disintegration_blocks))
