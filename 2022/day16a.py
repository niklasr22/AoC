from collections import defaultdict

import aocutils

valves = aocutils.read_lines("./2022/inputs/day16.txt")
valves = {
    v[6:8]: {
        "flow": int(v[23 : v.find(";")]),
        "neighbours": v[v.find(" ", v.find("valve")) + 1 :].split(", "),
    }
    for v in valves
}

# calc dists between each node for a graph that has direct edges to others
weights = defaultdict(lambda: float("inf"))
for v, d in valves.items():
    for n in d["neighbours"]:
        weights[(v, n)] = 1
dists = weights.copy()
for k in valves:
    for i in valves:
        for j in valves:
            if i != j:
                dists[(i, j)] = min(dists[(i, j)], dists[(i, k)] + dists[(k, j)])

# remove flow 0 valves
reduced_valves = {}
new_weights = {}
for v, data in valves.items():
    if data["flow"] > 0:
        reduced_valves[v] = data["flow"]
    else:
        for (i, j), distance in dists.items():
            # remove edges that have a length greater equal 29 (those take too much time anyway)
            if i != v and j != v and distance < 29:
                new_weights[(i, j)] = distance

AVAILABLE_TIME = 30
# brute force any way
def open_valve(time, current_flow, pressure, node, closed_valves) -> int:
    if time > AVAILABLE_TIME or time + 1 > AVAILABLE_TIME:
        return pressure
    # add open valve time and add flow
    time += 1
    pressure += current_flow  # pressure that is released during opening the valve
    current_flow += reduced_valves[node]

    new_closed_valves = set(closed_valves)
    new_closed_valves.remove(node)

    # if now all valves are open, just release pressure
    if len(new_closed_valves) == 0:
        return pressure + (AVAILABLE_TIME - time) * current_flow

    # try all paths
    new_max_pressure = -1
    for next in new_closed_valves:
        if time + new_weights[(node, next)] < AVAILABLE_TIME:
            press = open_valve(
                time=time + new_weights[(node, next)],
                current_flow=current_flow,
                pressure=pressure
                + new_weights[(node, next)]
                * current_flow,  # pressure that is released while traveling
                node=next,
                closed_valves=new_closed_valves,
            )
            new_max_pressure = max(new_max_pressure, press)
        else:
            new_max_pressure = max(
                new_max_pressure, pressure + (AVAILABLE_TIME - time) * current_flow
            )
    return new_max_pressure


max_pressure = -1
closed_valves = set(reduced_valves.keys())
for starting_valve in reduced_valves:
    press = open_valve(
        dists[("AA", starting_valve)], 0, 0, starting_valve, closed_valves
    )
    max_pressure = max(max_pressure, press)

print(max_pressure)
