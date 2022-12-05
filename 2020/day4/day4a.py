import re

file = open("./2020/day4/input.txt")
data = file.read()

passports = list(
    map(
        lambda x: list(map(lambda y: y.split(":"), re.split("\n| ", x))),
        data.strip(" \n").split("\n\n"),
    )
)

count = 0
for p in passports:
    fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for i, x in p:
        try:
            fields.remove(i)
        except:
            pass
    if len(fields) == 0:
        count += 1
print(count)
