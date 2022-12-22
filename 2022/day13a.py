import aocutils

pairs = aocutils.read_lineblocks("./2022/inputs/day13.txt")


def comp_list(l1, l2):
    for i in range(min(len(l1), len(l2))):
        if type(l1[i]) == type(l2[i]) == int:
            if l1[i] != l2[i]:
                return 1 if l1[i] < l2[i] else 0
        elif type(l1[i]) == type(l2[i]) == list:
            res = comp_list(l1[i], l2[i])
            if res != 2:
                return res
        else:
            nl1 = l1[i] if type(l1[i]) == list else [l1[i]]
            nl2 = l2[i] if type(l2[i]) == list else [l2[i]]
            res = comp_list(nl1, nl2)
            if res != 2:
                return res
    return 1 if len(l1) < len(l2) else (2 if len(l1) == len(l2) else 0)


def right_order_packets(pair):
    packet_1 = eval(pair[0])
    packet_2 = eval(pair[1])
    return True if comp_list(packet_1, packet_2) == 1 else False


right_order_indices = [i + 1 for i, p in enumerate(pairs) if right_order_packets(p)]
print(sum(right_order_indices))
