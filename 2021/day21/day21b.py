from collections import defaultdict

p1pos = 7
p2pos = 10

"""p1pos = 4
p2pos = 8"""

universes = {}

pInCharge = 0
def play(p1pos, p2pos, p1score, p2score):
    global universes
    if p1score >= 21:
        return (1, 0)
    elif p2score >= 21:
        return (0, 1)
    if (p1pos, p2pos, p1score, p2score) in universes:
        return universes[(p1pos, p2pos, p1score, p2score)]
    
    wins = (0,0)
    for d1 in range(1, 4):
        for d2 in range(1, 4):
            for d3 in range(1, 4):
                np1pos = (p1pos + d1 + d2 + d3 - 1) % 10 +1
                np1score = p1score + np1pos

                w1, w2 = play(p2pos, np1pos, p2score, np1score)
                wins = (wins[0] + w2, wins[1] + w1)
    universes[(p1pos, p2pos, p1score, p2score)] = wins
    return wins

p1wins, p2wins = play(p1pos,p2pos, 0, 0)

print("p1",p1wins)
print("p2",p2wins)

