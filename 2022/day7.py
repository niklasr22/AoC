import aocutils

lines = aocutils.read_lines("./2022/inputs/day7.txt")

root_dir = {}
all_dirs = [root_dir]

parents = []
current_dir = root_dir
for l in lines:
    if l == "$ ls":
        pass
    elif l.startswith("$ cd"):
        change_to = l[5:]
        if change_to == "..":
            current_dir = parents.pop()
        elif change_to == "/":
            parents.clear()
            current_dir = root_dir
        else:
            parents.append(current_dir)
            current_dir = current_dir[change_to]
    elif l.startswith("dir"):
        if l[4:] not in current_dir:
            current_dir[l[4:]] = {}
            all_dirs.append(current_dir[l[4:]])
    else:
        file_size, file_name = l.split(" ", 2)
        if l.split(" ")[0] not in current_dir:
            current_dir[file_name] = int(file_size)


def calc_dir_sizes(wd: dict) -> tuple[int, int]:
    size = 0
    del_candidates_size = 0
    for content in wd.values():
        if type(content) == int:
            size += content
        else:
            d_size, d_cc = calc_dir_sizes(content)
            size += d_size
            del_candidates_size += d_cc
    wd["____size"] = size

    if size <= 100000:
        del_candidates_size += size

    return size, del_candidates_size


total_size, dcs = calc_dir_sizes(root_dir)

unused_space = 70000000 - total_size
needed_space = 30000000 - unused_space

filtered_candidates = filter(lambda x: x["____size"] > needed_space, all_dirs)
del_cand = sorted(filtered_candidates, key=lambda x: x["____size"])

print("a", dcs, "b", del_cand[0]["____size"])
