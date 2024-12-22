from pathlib import Path

data = list(map(int, Path("2024/inputs/day22.txt").read_text().strip().splitlines()))


def next_secret(s):
    s = (s ^ (s << 6)) & 0xFFFFFF
    s = (s ^ (s >> 5)) & 0xFFFFFF
    s = (s ^ (s << 11)) & 0xFFFFFF
    return s


res = 0
for monkey in data:
    s = monkey
    for _ in range(2000):
        s = next_secret(s)
    print(s)
    res += s

print(res)
