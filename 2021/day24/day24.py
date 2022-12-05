from functools import lru_cache

# input
params = [
    (13, 10, 1),
    (11, 16, 1),
    (11, 0, 1),
    (10, 13, 1),
    (-14, 7, 26),
    (-4, 11, 26),
    (11, 11, 1),
    (-3, 10, 26),
    (12, 16, 1),
    (-12, 8, 26),
    (13, 15, 1),
    (-12, 2, 26),
    (-15, 5, 26),
    (-12, 10, 26),
]


def digitroutineC(z, d, pos):
    p = params[pos]
    x = z % 26 + p[0]
    z //= p[2]
    if x != d:
        z = z * 26 + d + p[1]
    return z


@lru_cache(maxsize=None)
def search(cpos, z):
    if cpos == 14:
        if z == 0:
            return [""]
        return []
    res = []
    for i in range(1, 10):
        newz = digitroutineC(z, i, cpos)
        r = search(cpos + 1, newz)
        for rr in r:
            res.append(str(i) + rr)
    return res


res = search(0, 0)
res = [int(x) for x in res]
print("a)", max(res))
print("b)", min(res))
