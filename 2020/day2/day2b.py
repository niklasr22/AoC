file = open("./2020/day2/input.txt")
data = file.read()

rows = list(filter(lambda x : x != '', data.split("\n")))
valid = 0
for pw in rows:
    s = pw.split("-")
    pos1 = int(s[0])
    s = s[1].split(" ");
    pos2 = int(s[0])
    password = s[2]
    c = s[1][0]
    if (password[pos1 - 1] == c and password[pos2 - 1] != c) or (password[pos1 - 1] != c and password[pos2 - 1] == c):
        valid += 1

print(valid, "valid passwords")

