from pathlib import Path

workflows, parts = Path("2023/inputs/day19.txt").read_text().split("\n\n")


def parse_part(part):
    properties = part[1:-1].split(",")
    return {
        property.split("=")[0]: int(property.split("=")[1]) for property in properties
    }


def parse_wf(wf: str):
    rules = wf[wf.index("{") + 1 : -1].split(",")
    rules_dict = {}
    for rule in rules:
        if ":" in rule:
            cond, dest = rule.split(":")
            rules_dict[cond] = dest
        else:
            rules_dict["basis"] = rule

    return wf[: wf.index("{")], rules_dict


def apply(part, wf):
    for rule, dest in wf.items():
        if rule == "basis":
            return dest
        op = rule[1]
        param = rule[0]
        val = int(rule[2:])
        if op == ">" and part[param] > val:
            return dest
        elif op == "<" and part[param] < val:
            return dest


workflows = {
    name: rules
    for name, rules in [parse_wf(workflow) for workflow in workflows.splitlines()]
}
parts = [parse_part(part) for part in parts.splitlines()]

accepted = []
for part in parts:
    next_wf = "in"
    while next_wf not in ["A", "R"]:
        wf = workflows[next_wf]
        next_wf = apply(part, wf)
    if next_wf == "A":
        accepted.append(part)

print(sum(sum(props.values()) for props in accepted))
