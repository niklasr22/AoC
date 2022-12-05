data = open("./2021/day10/input.txt").read()
rows = data.splitlines()

open_to_close = {"(": ")", "[": "]", "<": ">", "{": "}"}
open_chars = open_to_close.keys()
score_corrupted = {")": 3, "]": 57, "}": 1197, ">": 25137}
score_incomplete = {")": 1, "]": 2, "}": 3, ">": 4}

incomplete_scores = []
corrupted_score = 0
for r in rows:
    q = []
    corrupted = False
    for c in r:
        if c in open_chars:
            q.append(open_to_close[c])
        else:
            last = q.pop()
            if c != last:
                corrupted = True
                corrupted_score += score_corrupted[c]
                break
    if not corrupted and len(q) != 0:  # incomplete
        q.reverse()
        t = 0
        for c in q:
            t *= 5
            t += score_incomplete[c]
        incomplete_scores.append(t)

incomplete_scores.sort()
print("corrupted score\t\t", corrupted_score)
print("incomplete score\t", incomplete_scores[len(incomplete_scores) // 2])
