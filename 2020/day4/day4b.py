import re

file = open("./2020/day4/input.txt")
data = file.read()

passports = list(map(lambda x : list(map(lambda y: y.split(":"), re.split("\n| ", x))), data.strip(" \n").split("\n\n")))

eyecolors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
count = 0
for p in passports:
    fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for i,x in p:
        if i == "byr":
            if not(len(x) == 4 and int(x) >= 1920 and int(x) <= 2002):
                break
        if i == "iyr":
            if not(len(x) == 4 and int(x) >= 2010 and int(x) <= 2020):
                break
        if i == "eyr":
            if not(len(x) == 4 and int(x) >= 2020 and int(x) <= 2030):
                break
        if i == "hgt":
            if x.endswith("in") and int(x[:-2]) >= 59 and int(x[:-2]) <= 76:
                pass
            elif x.endswith("cm") and int(x[:-2]) >= 150 and int(x[:-2]) <= 193:
                pass
            else:
                break
        if i == "hcl":
            if re.match("#[a-f0-9]{6}", x) == None:
                break
        if i == "ecl":
            try:
                eyecolors.index(x)
            except:
                break
        if i == "pid":
            if len(x) != 9 or not x.isnumeric():
                break
        try:
            fields.remove(i)
        except:
            pass
    if len(fields) == 0:
        count += 1
print(count)