data = open("./2021/day8/input.txt").read()
rows = list(map(lambda x : x.split(" | "), data.splitlines()))

def strdiff(a: str, b: str) -> str:
    notfound = ''
    for i in a:
        if b.find(i) == -1:
            notfound += i
    return notfound
    

def charr(word):
    return "".join(list(sorted([char for char in word])))

sum = 0

count = 0
for r in rows:
    pass