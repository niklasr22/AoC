from pathlib import Path

data = list(map(int, Path("2024/inputs/day22.txt").read_text().strip().splitlines()))


def next_secret(s):
    s = (s ^ (s << 6)) & 0xFFFFFF
    s = (s ^ (s >> 5)) & 0xFFFFFF
    s = (s ^ (s << 11)) & 0xFFFFFF
    return s


monkeys = []
for monkey in data:
    s = monkey
    monkey_prices = [monkey % 10]
    for _ in range(2000):
        s = next_secret(s)
        monkey_prices.append(s % 10)

    monkey_diffs = [
        monkey_prices[i] - monkey_prices[i - 1] for i in range(1, len(monkey_prices))
    ]
    monkey_offers = {}
    for i in range(len(monkey_diffs) - 4):
        seq = tuple(monkey_diffs[i : i + 4])
        if seq in monkey_offers:
            continue
        monkey_offers[seq] = monkey_prices[i + 4]
    monkeys.append(monkey_offers)


all_seqs = set([seq for monkey in monkeys for seq in monkey.keys()])
values = {
    seq: sum(monkey_offers.get(seq, 0) for monkey_offers in monkeys) for seq in all_seqs
}
max_seq = max(values, key=values.get)
print(max_seq, values[max_seq])
