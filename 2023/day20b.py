import copy
from collections import defaultdict
from pathlib import Path

import networkx as nx

modules_strs = Path("2023/inputs/day20.txt").read_text().splitlines()

modules = {}
state = {}

edges = []

input_edges_counter = defaultdict(list)

for module_str in modules_strs:
    name, neighbours = module_str.split(" -> ")
    base_name = name
    if name == "broadcaster":
        mod_type = "bc"
    elif not name[0].isalpha():
        mod_type = name[0]
        name = name[1:]
    modules[name] = {"type": mod_type, "neighbours": neighbours.split(", ")}
    for neighbour in modules[name]["neighbours"]:
        input_edges_counter[neighbour].append(name)

for module, props in modules.items():
    if props["type"] == "%":
        state[module] = False
    elif props["type"] == "&":
        state[module] = {
            input_node: False for input_node in input_edges_counter[module]
        }

# plot network
# for module, data in modules.items():
#     for neighbour in data["neighbours"]:
#         neighbourname = f'{(modules[neighbour]["type"] if neighbour in modules else "")} {neighbour}'
#         print(neighbourname)
#         neighbourname = neighbourname.replace("%", "ff")
#         edges.append((f'{data["type"].replace("%", "ff")} {module}', neighbourname))

# G = nx.DiGraph()
# G.add_edges_from(edges)


# PG = nx.nx_pydot.to_pydot(G)
# PG.write_png("output.png")


def process_pulse(pulse, receiver, sender) -> tuple[int, int]:
    pulses = {True: 0, False: 0}

    queue = [(pulse, receiver, sender)]

    rx_reached = False

    while queue and not rx_reached:
        pulse, receiver, sender = queue.pop(0)

        if receiver in ["js", "rr", "bs", "zb"]:
            if pulse == False:
                print(receiver, pulse, "presses", presses)
            continue

        new_pulse = False
        if receiver == "broadcaster":
            new_pulse = pulse
        elif modules[receiver]["type"] == "%":
            if not pulse:
                current_state = state[receiver]
                state[receiver] = not current_state
                new_pulse = state[receiver]
            else:
                continue
        elif modules[receiver]["type"] == "&":
            state[receiver][sender] = pulse
            new_pulse = not all(state[receiver].values())

        for neighbour in modules[receiver]["neighbours"]:
            # print(receiver, f"-{new_pulse}->", neighbour)
            pulses[new_pulse] += 1
            if neighbour == "rx" and new_pulse == False:
                print("reached rx")
                rx_reached = True
            if neighbour in modules:
                queue.append((new_pulse, neighbour, receiver))

    return pulses[True], pulses[False], rx_reached


reached = False
presses = 1

ref_state = copy.deepcopy(state)

while not reached:
    _, _, _ = process_pulse(False, "broadcaster", "btn")

    presses += 1

# solution sketch :
# 1. find subgraphs which connect to rx via some conjunctions
# 2. check what the output of the output conjunction of each subgraph has to be
# 3. find the button press cycles with the need output for each subgraph
# 4. lcm of the cycle lenghts
