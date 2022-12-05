from collections import defaultdict

data = open("./2021/day12/input.txt").read()
rows = list(map(lambda x: x.split("-"), data.splitlines()))
graph = defaultdict(lambda: [])
nodes = dict()
counter = 0
twice = True

for r in rows:
    r1, r2 = r
    if not r1 in nodes:
        nodes[r1] = 0
    if not r2 in nodes:
        nodes[r2] = 0
    graph[r1].append(r2)
    graph[r2].append(r1)


def walk(sn: str):
    global counter, twice
    if sn == "end":
        counter += 1
        return
    if sn == "start" and nodes[sn] != 0:
        return
    if sn.islower():
        nodes[sn] += 1
        twice = True if nodes[sn] == 2 else twice
    for n in graph[sn]:
        if nodes[n] < 1 or (nodes[n] == 1 and twice == False):
            walk(n)
    if sn.islower():
        nodes[sn] -= 1
        twice = False if nodes[sn] == 1 else twice


walk("start")
print("a: ", counter)
counter = 0
twice = False
walk("start")
print("b: ", counter)
