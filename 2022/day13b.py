import aocutils
import functools

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


def packet_sort(p1, p2):
    return -1 if comp_list(p1, p2) == 1 else 1


packets = [eval(p) for p in aocutils.flatten(pairs)] + [[[2]], [[6]]]

packets = sorted(packets, key=functools.cmp_to_key(packet_sort))
print((packets.index([[2]]) + 1) * (packets.index([[6]]) + 1))
