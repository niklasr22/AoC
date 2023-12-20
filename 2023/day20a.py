from collections import defaultdict
from pathlib import Path

modules_strs = Path("2023/inputs/day20.txt").read_text().splitlines()

modules = {}
state = {}

input_edges_counter = defaultdict(list)

for module_str in modules_strs:
    name, neighbours = module_str.split(" -> ")
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

print(state)


def process_pulse(pulse, receiver, sender) -> tuple[int, int]:
    pulses = {True: 0, False: 0}

    queue = [(pulse, receiver, sender)]

    while queue:
        pulse, receiver, sender = queue.pop(0)

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
            if neighbour in modules:
                queue.append((new_pulse, neighbour, receiver))

    return pulses[True], pulses[False]


h_total, l_total = 0, 0

for _ in range(1000):
    h, l = process_pulse(False, "broadcaster", "btn")
    # print(state)
    # print("---")
    h_total += h
    l_total += l + 1  # +1 for button pulse

print(h_total, l_total, h_total * l_total)
