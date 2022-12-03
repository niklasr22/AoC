import aocutils

elves = aocutils.read_lineblocks("./2022/inputs/day1.txt", apply_on_line=int)
elves = [sum(e) for e in elves]
print("1st:", max(elves))
print("2nd:", sum(sorted(elves, reverse=True)[:3]))