from pathlib import Path

cards = Path("2023/inputs/day4a.txt").read_text().splitlines()

# replace multiple whitespaces by one
cards = [card.replace("  ", " ") for card in cards]

result = 0
for card in cards:
    lists = card[card.index(":") :]
    winning_txt, own_txt = lists.split("|")
    winning = set(winning_txt.strip().split(" "))
    own = set(own_txt.strip().split(" "))

    winners = own.intersection(winning)
    if len(winners) > 0:
        result += 1 * 2 ** (len(winners) - 1)

print(result)
