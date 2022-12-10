import aocutils

instructions = aocutils.read_lines("./2022/inputs/day10.txt")

cycles_of_interest = [20, 60, 100, 140, 180, 220]
signal_sum = 0
x = 1
cycle = 0

def add_signal_strength() -> tuple[int, bool]:
    if cycle == cycles_of_interest[0]:
        signal = x * cycle
        cycles_of_interest.pop(0)
        if len(cycles_of_interest) == 0:
            return signal, True
        return signal, False
    return 0, False

for instruction in instructions:
    stop = False
    signal = 0
    if instruction == "noop":
        cycle += 1
        signal, stop = add_signal_strength()
    elif instruction.startswith("addx"):
        v = int(instruction[5:])
        cycle += 1
        signal, stop = add_signal_strength()
        signal_sum += signal
        if stop:
            break
        cycle += 1
        signal, stop = add_signal_strength()
        x += v 
    signal_sum += signal
    if stop:
        break

print(signal_sum)