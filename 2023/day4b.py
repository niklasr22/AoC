from collections import defaultdict
from pathlib import Path

cards = Path("2023/inputs/day4a.txt").read_text().splitlines()

# replace multiple whitespaces by one
cards = [card.replace("  ", " ") for card in cards]

instances = {i: 1 for i in range(len(cards))}

for i, card in enumerate(cards):
    lists = card[card.index(":") :]
    winning_txt, own_txt = lists.split("|")
    winning = set(winning_txt.strip().split(" "))
    own = set(own_txt.strip().split(" "))

    winners = own.intersection(winning)

    for copy in range(i + 1, i + 1 + len(winners)):
        if copy < len(cards):
            instances[copy] += 1 * instances[i]
print(sum(instances.values()))
