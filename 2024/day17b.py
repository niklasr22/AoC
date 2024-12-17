import re
from pathlib import Path

data = Path("2024/test/day17.txt").read_text().strip()

program = "2,4,1,1,7,5,0,3,4,7,1,6,5,5,3,0"

program = list(map(int, re.findall(r"\d+", program)))


def get_combo_val(op, registers):
    if op <= 3:
        return op
    if op == 4:
        return registers["A"]
    if op == 5:
        return registers["B"]
    if op == 6:
        return registers["C"]
    raise ValueError(f"Unknown op: {op}")


def run(program, registers):
    outputs = []
    ip = 0
    while ip < len(program):
        instr = program[ip]
        op = program[ip + 1]

        if instr == 0:  # div
            op = get_combo_val(op, registers)
            registers["A"] = registers["A"] // (2**op)
        elif instr == 1:  # bxl
            registers["B"] = registers["B"] ^ op
        elif instr == 2:  # bst
            op = get_combo_val(op, registers)
            registers["B"] = op % 8
        elif instr == 3:  # jnz
            if registers["A"] != 0:
                ip = op
                continue
        elif instr == 4:  # bxc
            registers["B"] = registers["B"] ^ registers["C"]
        elif instr == 5:  # out
            op = get_combo_val(op, registers)
            outputs.append(op % 8)
        elif instr == 6:  # bdv
            op = get_combo_val(op, registers)
            registers["B"] = registers["A"] // (2**op)
        elif instr == 7:  # cdv
            op = get_combo_val(op, registers)
            registers["C"] = registers["A"] // (2**op)

        ip += 2
    return outputs


def discover(pos: int, i: int):
    if pos < 0:
        return
    possibilities = []
    for t in range(0, 8):
        new_i = (i << 3) + t
        output = run(program, {"A": new_i, "B": 0, "C": 0})
        if output[0] == program[pos]:
            if pos == 0 and output == program:
                return new_i
            possibilities.append(t)

    if len(possibilities) >= 1:
        return min(
            discover(pos - 1, (i << 3) + possibility) for possibility in possibilities
        )

    return float("inf")


i = discover(pos=len(program) - 1, i=0)
print("B:", i)
print(program)
print(run(program, {"A": i, "B": 0, "C": 0}))
