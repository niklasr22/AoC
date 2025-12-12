from pathlib import Path

data = Path("2025/inputs/day12.txt").read_text().strip()

presents = []
present_areas = []
trees = []

blocks = data.split("\n\n")
for block in blocks[:-1]:
    block = block.splitlines()
    presents.append([[1 if c == "#" else 0 for c in l] for l in block[1:]])
    present_areas.append(sum(sum(presents[-1][i]) for i in range(3)))

for line in blocks[-1].splitlines():
    width, height = list(map(int, line.split(":")[0].split("x")))
    trees.append(
        {
            "w": width,
            "h": height,
            "shapes": list(map(int, line.split(":")[1].strip().split(" "))),
        }
    )

filtered_trees = []
for tree in trees:
    present_area = sum(
        count * present_areas[shape] for shape, count in enumerate(tree["shapes"])
    )
    if tree["w"] * tree["h"] > present_area:
        filtered_trees.append(tree)

print(len(filtered_trees))
