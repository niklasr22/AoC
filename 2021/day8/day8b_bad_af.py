import time

data = open("./2021/day8/input.txt").read()
rows = list(map(lambda x : x.split(" | "), data.splitlines()))

def strdiff(a: str, b: str) -> str:
    notfound = ''
    for i in a:
        if b.find(i) == -1:
            notfound += i
    return notfound
    

def charr(word):
    return "".join(list(sorted([char for char in word])))

correct = dict()
correct["abcefg"] = 0
correct["cf"] = 1
correct["acdeg"] = 2
correct["acdfg"] = 3
correct["bcdf"] = 4
correct["abdfg"] = 5
correct["abdefg"] = 6
correct["acf"] = 7
correct["abcdefg"] = 8
correct["abcdfg"] = 9

sumall = 0

start = time.time()

count = 0
for r in rows:
    letters = dict()
    letters['a'] = ''
    letters['b'] = ''
    letters['c'] = ''
    letters['d'] = ''
    letters['e'] = ''
    letters['f'] = ''
    letters['g'] = ''
    v = dict()
    v[0] = ''
    v[1] = ''
    v[2] = ''
    v[3] = ''
    v[4] = ''
    v[5] = ''
    v[6] = ''
    v[7] = ''
    v[8] = ''
    v[9] = ''
    dd = r[0].split(" ")
    digits = r[1].split(" ")
    dd += digits
    for u in range(8):
        for d in dd:
            if len(d) == 2:
                v[1] = d
            elif len(d) == 3:
                v[7] = d
                if v[1] != '':
                    letters['a'] = strdiff(d, v[1])
            elif len(d) == 4:
                v[4] = d
            elif len(d) == 7:
                v[8] = d
            elif len(d) == 6 and v[1] != '': # 6 and 9
                x = strdiff(v[1], d)
                if x != '': #6
                    letters['c'] = x
                    v[6] = d
                elif v[4] != '' and len(strdiff(v[4], d)) == 0: #9
                    v[9] = d
                    letters['e'] = strdiff("abcdefg", d)
                else: #0
                    v[0] = d
                    letters['d'] = strdiff("abcdefg", d)
                    if v[4] != '' and v[1] != '':
                        letters['b'] = strdiff(v[4], v[1]).replace(letters['d'], "")
            elif len(d) == 5: # 5
                if v[5] != '' and d != v[5] and letters['f'] != '' and d.find(letters['f']) != -1:
                    v[3] = d
                    if v[4] != '' and v[7] != '':
                        letters['g'] = strdiff(strdiff(d, v[4]), v[7])
                elif letters['e'] != '' and d.find(letters['e']) != -1:
                    v[2] = d
                    letters['b'] = strdiff("abcdefg", d).replace(letters['f'], "")
                elif letters['b'] != '' and d.find(letters['b']) != -1:
                    v[5] = d
                    letters['b'] = strdiff("abcdefg", d).replace(letters['f'], "")
                    if v[6] != '':
                        letters['e'] = strdiff(v[6], d)
                elif letters['f'] != '' and d.find(letters['f']) == -1:
                    v[2] = d
                    letters['b'] = strdiff("abcdefg", d).replace(letters['f'], "")
                elif letters['c'] != '' and d.find(letters['c']) == -1:
                    v[5] = d
                    if letters['f'] != '':
                        letters['b'] = strdiff("abcdefg", d).replace(letters['f'], "")
                    if v[6] != '':
                        letters['e'] = strdiff(v[6], d)
                
                if d != v[2] and d != v[5] and v[5] != '' and v[2] != '':
                    v[3] = d
                    if v[4] != '' and v[7] != '':
                        letters['g'] = strdiff(strdiff(d, v[4]), v[7])

    emptyC = 0
    lk = -1
    for k,val in v.items():
        if val == '':
            lk = k
            emptyC += 1

    tab = dict()
    for x, y in letters.items():
        tab[y] = x

    value = ''

    tabD = dict()
    for k,val in v.items():
        tabD[charr(val)] = k

    for d in digits:
        x = charr(d)
        if x in tabD.keys():
            value += str(tabD[x])
        elif emptyC == 1:
            value += str(lk)
        else:
            wire = ""
            for i in x:
                if i in tab.keys():
                    wire += tab[i]
            wire = charr(wire)
            if wire in correct:
                value += str(correct[wire])
    print(value)
    sumall += int(value)
print(sumall)

print(time.time()-start)