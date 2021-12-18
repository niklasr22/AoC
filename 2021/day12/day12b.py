from collections import defaultdict

data = open("./2021/day12/input2.txt").read()
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
twice = False
def walk(sn: str):
    global counter, twice
    if sn == "end":
        counter += 1
        return
    if sn == "start" and nodes[sn] != 0:
        return
    if sn.islower():
        nodes[sn] += 1
        if nodes[sn] == 2:
            twice = True
    for n in graph[sn]:
        if nodes[n] < 1 or (nodes[n] == 1 and twice == False):
            walk(n)
    if sn.islower():
        nodes[sn] -= 1
        if nodes[sn] == 1:
            twice = False

walk("start")
print(counter)