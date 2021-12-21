from collections import defaultdict

p1pos = 7
p2pos = 10
"""p1pos = 4
p2pos = 8"""

p1score = 0
p2score = 0

diceRolls = 0

dice = 1
def dicePoints():
    global dice, diceRolls
    s = 0
    for _ in range(3):
        s += dice
        dice += 1
        dice = ((dice - 1) % 100)+1
        diceRolls += 1
    return s

pInCharge = 0
while p1score < 1000 and p2score < 1000:
    if pInCharge == 0:
        p1pos = ((p1pos + dicePoints() - 1) % 10) + 1
        p1score += p1pos
        pInCharge = 1
        print("p1",p1pos,diceRolls,p1score)
    elif pInCharge == 1:
        p2pos = ((p2pos + dicePoints() - 1) % 10) + 1
        p2score += p2pos
        print("p2",p2pos,diceRolls,p2score)
        pInCharge = 0
print(p1score * diceRolls, p1score, diceRolls)
print(p2score * diceRolls, p2score)
