import re
from pathlib import Path

data = Path("2024/inputs/day17.txt").read_text().strip()

registers, program = data.split("\n\n")

register_values = list(map(int, re.findall(r"\d+", registers)))
registers = {"A": register_values[0], "B": register_values[1], "C": register_values[2]}
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


print(",".join(map(str, run(program, registers))))
