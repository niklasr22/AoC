from collections import defaultdict

p1pos = 7
p2pos = 10

p1pos = 4
p2pos = 8

p1score = 0
p2score = 0

p1wins = 0
p2wins = 0

universes = []

p1scores = defaultdict(lambda:0)
p2scores = defaultdict(lambda:0)

p1scores[0] = 1
p2scores[0] = 1
pInCharge = 0
while True:
    if pInCharge == 0:
        for s,c in p1scores.items():
            if s >= 21:
                continue
            for d in range(3, 10):
                p1pos = ((p1pos + d - 1) % 10) + 1
                score = s + p1pos
                p1scores[p1scores] += 1
                p1scores[s] -= 1
                pInCharge = 1
    elif pInCharge == 1:
        for s,c in p2scores.items():
            if s >= 21:
                continue
            for d in range(3, 10):
                p2pos = ((p2pos + d - 1) % 10) + 1
                score = s + p2pos
                p1scores[p2scores] += 1
                p1scores[s] -= 1
                pInCharge = 1

