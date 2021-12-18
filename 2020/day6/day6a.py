file = open("./2020/day6/input.txt")
data = file.read()

groups = list(map(lambda x : x.splitlines(), data.split("\n\n")))


count = 0
for g in groups:
    questions = set()
    for p in g:
        for c in p:
            questions.add(c)
    count += len(questions)

print(count)