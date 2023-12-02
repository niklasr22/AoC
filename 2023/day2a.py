from pathlib import Path

games = Path("2023/inputs/day2.txt").read_text().splitlines()

AVAILABLITY = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def clean(grab_item: str) -> tuple[str, int]:
    data = grab_item.strip().split(" ")
    return data[1], int(data[0])


def is_possible(game):
    for grab in game:
        for color in grab:
            if AVAILABLITY[color[0]] < color[1]:
                return False
    return True


games = {
    int(game[5 : game.index(":")]): [
        list(map(clean, grab.split(",")))
        for grab in game[game.index(":") + 1 :].split(";")
    ]
    for game in games
}

result = 0
for id, game in games.items():
    if is_possible(game):
        result += id

print(result)
