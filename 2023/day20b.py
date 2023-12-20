import copy
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

    rx_reached = False

    while queue and not rx_reached:
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
            if neighbour == "rx" and new_pulse == False:
                print("reached rx")
                rx_reached = True
            if neighbour in modules:
                queue.append((new_pulse, neighbour, receiver))

    return pulses[True], pulses[False], rx_reached


h_total, l_total = 0, 0
reached = False
presses = 0


d = {...}
ref_state = copy.deepcopy(state)


while not reached:
    h, l, reached = process_pulse(False, "broadcaster", "btn")

    if state == ref_state:
        print(state == ref_state, "state is the same")

    presses += 1
    if reached:
        print("RX after: ", presses + 1)
    # print(state)
    # print("---")
    h_total += h
    l_total += l + 1  # +1 for button pulse

print(h_total, l_total, h_total * l_total)


# idea:

# 1. find cycles for each module on the path to rx
# 2. lcm for each stage
