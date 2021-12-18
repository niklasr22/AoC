from collections import defaultdict
file = open("./2020/day6/input.txt")
data = file.read()
groups = list(map(lambda x : x.splitlines(), data.split("\n\n")))
count = 0
for g in groups:
    questions = defaultdict(lambda : 0)
    answers = set()
    for p in g:
        for c in p:
            questions[c] += 1
    x = len(g)
    for a, b in questions.items():
        if b == x:
            answers.add(a)
    count += len(answers)
print(count)