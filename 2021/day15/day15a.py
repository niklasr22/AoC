from collections import Counter
from collections import defaultdict
data = open("./2021/day15/input.txt").read()
rows = data.splitlines()

h = [-1, 0, 1, 0]
v = [0, 1, 0, -1]

width = len(rows[0])
height = len(rows)

dist = []
predecessors = {}
nodes = {}

def initd(sx,sy):
    for y in range(len(rows)):
        for x in range(len(rows[y])):
            predecessors[(x,y)] = None
            nodes[(x,y)] = float("inf")
    nodes[(sx,sy)] = 0
    
def distanceupdate(u, uval, v):
    alt = uval + int(rows[v[1]][v[0]])
    if alt < nodes[v]:
        nodes[v] = alt
        predecessors[v] = u

def dijkstra(x,y,tx,ty):
    initd(x,y)
    while len(nodes) > 0:
        u = min(nodes, key=nodes.get)
        uval = nodes.pop(u)
        if u[0] == tx and u[1] == ty:
            print(uval)
            break
        for i in range(4):
            xx = u[0] + h[i]
            yy = u[1] + v[i]
            if (xx, yy) in nodes:
                distanceupdate(u, uval, (xx,yy))
    return predecessors
        
def shortest(s, t):
    way = [t]
    u = t
    while predecessors[u] != None:
        u = predecessors[u]
        way.insert(0, u)
    
    d = 0
    for i in way:
        d += int(rows[i[1]][i[0]])
    return d - int(rows[s[1]][s[0]])

#print(walk(0,0,0),oalr)
dijkstra(0,0,width-1, height-1)
print("finished dijkstra")
print(shortest((0,0),(width-1,height-1)))
