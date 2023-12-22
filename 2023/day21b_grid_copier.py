from pathlib import Path

grid = Path("2023/inputs/day21.txt").read_text().splitlines()

copies = 3
new_grid = []

for y_c in range(copies):
    for y in range(len(grid)):
        new_grid.append(grid[y] * copies)

grid_txt = "\n".join(new_grid)
grid_txt = grid_txt.replace("S", ".", (copies * copies) // 2)
grid_txt = grid_txt[: grid_txt.find("S") + 1] + grid_txt[
    grid_txt.find("S") + 1 :
].replace("S", ".")


Path(f"2023/inputs/day21_real_sq{copies}x{copies}.txt").write_text(grid_txt)
