import aocutils
import functools

monkey_inputs = aocutils.read_blocks("./2022/inputs/day11.txt")


def mul(op1: int, op2: int) -> int:
    return op1 * op2


def add(op1: int, op2: int) -> int:
    return op1 + op2


def ggt(a: int, b: int) -> int:
    while b != 0:
        h = a % b
        a = b
        b = h
    return a


def kgv(a: int, b: int) -> int:
    return abs(a * b) / ggt(a, b)


class Monkey:
    def __init__(
        self,
        items: list[float],
        operators: list[str],
        operation: callable,
        test: int,
        true_dest: int,
        false_dest: int,
    ) -> None:
        self.items = items
        self.operators = operators
        self.operation = operation
        self.test = test
        self.true_dest = true_dest
        self.false_dest = false_dest
        self.inspections = 0

    def has_items(self) -> bool:
        return len(self.items) > 0

    def check_item(self, divisor) -> tuple[float, int] | None:
        if len(self.items) == 0:
            return None
        self.inspections += 1
        item = self.items.pop(0)
        operator1 = item if self.operators[0] == "old" else int(self.operators[0])
        operator2 = item if self.operators[2] == "old" else int(self.operators[2])
        new = self.operation(operator1, operator2) % divisor
        dest = self.true_dest if int(new % self.test) == 0 else self.false_dest
        return new, dest

    def add_item(self, item: int):
        self.items.append(item)


monkeys: list[Monkey] = list()

tests = []
for mi in monkey_inputs:
    lines: list[str] = mi.splitlines()
    items = list(map(float, lines[1].split(":")[1].strip().split(", ")))
    operators = lines[2].split("new = ")[1].split(" ")
    operation = mul if operators[1] == "*" else add
    test = int(lines[3].rsplit(" ", 1)[1])
    tests.append(test)
    true_dest = int(lines[4].rsplit(" ", 1)[1])
    false_dest = int(lines[5].rsplit(" ", 1)[1])
    monkeys.append(Monkey(items, operators, operation, test, true_dest, false_dest))


total_kgv = functools.reduce(lambda a, b: kgv(a, b), tests)

for round in range(10000):
    for m in monkeys:
        while m.has_items():
            res = m.check_item(total_kgv)
            if res is not None:
                new, dest = res
                monkeys[dest].add_item(new)

monkey_activity = sorted([m.inspections for m in monkeys])
print(monkey_activity)
print(monkey_activity[-2] * monkey_activity[-1])
