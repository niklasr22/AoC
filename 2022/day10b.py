import aocutils

instructions = aocutils.read_lines("./2022/inputs/day10.txt")

x = 1
cycle = 0

display = []


def draw(pixel, sprite_pos):
    px = (pixel - 1) % 40
    if sprite_pos - 1 <= px <= sprite_pos + 1:
        display.append("#")
    else:
        display.append(".")


for instruction in instructions:
    if instruction == "noop":
        cycle += 1
        draw(cycle, x)
    elif instruction.startswith("addx"):
        v = int(instruction[5:])
        cycle += 1
        draw(cycle, x)
        cycle += 1
        draw(cycle, x)
        x += v

print(cycle)

while len(display) > 0:
    print("".join(display[:40]))
    display = display[40:]
