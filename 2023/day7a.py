from collections import defaultdict
from pathlib import Path

translation_table = str.maketrans("AKQJT", "ZYXWV")
cards = list(
    map(
        lambda x: x.split(" "),
        Path("2023/inputs/day7.txt")
        .read_text()
        .translate(translation_table)
        .splitlines(),
    )
)


def check_type(card):
    different_cards = sorted(set(card), key=card.count)
    no_diff_cards = len(different_cards)
    if no_diff_cards == 1:
        return 7
    if no_diff_cards == 2 and card.count(different_cards[0]) == 1:
        return 6
    if no_diff_cards == 2 and card.count(different_cards[0]) == 2:
        return 5
    if no_diff_cards == 3 and card.count(different_cards[-1]) == 3:
        return 4
    if (
        no_diff_cards == 3
        and card.count(different_cards[-1]) == 2
        and card.count(different_cards[-2]) == 2
    ):
        return 3
    if no_diff_cards == 4:
        return 2
    return 1


types = defaultdict(list)
for card in cards:
    types[check_type(card[0])].append(card)

for key, cards_of_type in types.items():
    types[key] = sorted(cards_of_type, key=lambda x: x[0])

cards = []
for key in sorted(types.keys()):
    cards.extend(types[key])

result = 0
for i, card in enumerate(cards):
    result += (1 + i) * int(card[1])
print(result)
