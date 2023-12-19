from collections import defaultdict
from pathlib import Path

workflows, _ = Path("2023/inputs/day19.txt").read_text().split("\n\n")


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


workflows = {
    name: rules
    for name, rules in [parse_wf(workflow) for workflow in workflows.splitlines()]
}


def possibilities(xmas_ranges):
    pos = 1
    for r in xmas_ranges.values():
        pos *= r[1] - r[0] + 1
    return pos


def flow_split(flow, xmas_range):
    output = defaultdict(list)
    for rule, dest in flow.items():
        if rule == "basis":
            output[dest].append(xmas_range)
            continue

        op = rule[1]
        param = rule[0]
        val = int(rule[2:])
        out_xmas_range = xmas_range.copy()
        if op == ">" and xmas_range[param][1] > val:
            out_xmas_range[param] = (
                max(xmas_range[param][0], val + 1),
                xmas_range[param][1],
            )
            output[dest].append(out_xmas_range)
            xmas_range[param] = (
                xmas_range[param][0],
                max(xmas_range[param][0], val + 1) - 1,
            )
        elif op == "<" and xmas_range[param][0] < val:
            out_xmas_range[param] = (
                xmas_range[param][0],
                min(xmas_range[param][1], val - 1),
            )
            output[dest].append(out_xmas_range)
            xmas_range[param] = (
                min(xmas_range[param][1], val - 1) + 1,
                xmas_range[param][1],
            )

    accepted = sum(possibilities(r) for r in output["A"]) if "A" in output else 0

    for wf, wf_inranges in output.items():
        for wf_inrange in wf_inranges:
            if wf == "A" or wf == "R":
                continue
            accepted += flow_split(workflows[wf], wf_inrange)

    return accepted


flow = workflows["in"]
input_ranges = {"x": (1, 4000), "m": (1, 4000), "a": (1, 4000), "s": (1, 4000)}

print(flow_split(flow, input_ranges))
