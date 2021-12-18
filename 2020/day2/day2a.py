file = open("./2020/day2/input.txt")
data = file.read()

rows = list(filter(lambda x : x != '', data.split("\n")))
valid = 0
for pw in rows:
    s = pw.split("-")
    min = int(s[0])
    s = s[1].split(" ");
    max = int(s[0])
    password = s[2]
    c = s[1][0]
    count = password.count(c)
    if count >= min and count <= max:
        valid += 1

print(valid, "valid passwords")

