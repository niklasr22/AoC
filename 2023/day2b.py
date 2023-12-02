from pathlib import Path

games = Path("2023/inputs/day2.txt").read_text().splitlines()


def clean(grab_item: str) -> tuple[str, int]:
    data = grab_item.strip().split(" ")
    return data[1], int(data[0])


def power(game) -> int:
    cubes = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }
    for grab in game:
        for color in grab:
            cubes[color[0]] = max(color[1], cubes[color[0]])
    return cubes["red"] * cubes["blue"] * cubes["green"]


games = {
    int(game[5 : game.index(":")]): [
        list(map(clean, grab.split(",")))
        for grab in game[game.index(":") + 1 :].split(";")
    ]
    for game in games
}
result = sum(power(game) for game in games.values())

print(result)
