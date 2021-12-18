from collections import defaultdict

data = open("./2021/day12/input.txt").read()
rows = list(map(lambda x: x.split("-"), data.splitlines()))

graph = defaultdict(lambda : [])
nodes = dict()

for r in rows:
    r1, r2 = r
    if not r1 in nodes:
        nodes[r1] = 0
    if not r2 in nodes:
        nodes[r2] = 0
    graph[r1].append(r2)
    graph[r2].append(r1)

counter = 0

def walk(sn: str, path: list):
    global counter
    if sn == "end":
        counter += 1
        return
    if sn.islower():
        nodes[sn] = 1
    p = 0
    for n in graph[sn]:
        if nodes[n] != 1:
            walk(n, path)
            p += 1
    nodes[sn] = 0

walk("start", [])
print(counter)