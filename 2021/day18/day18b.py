import json
import copy
import math
data = open('./2021/day18/input.txt').read()
rows = list(map(json.loads, data.splitlines()))

def reduceHelper(a, x, d):
    if d == -1:
        for i in range(len(a)-1, -1, -1):
            if type(a[i]) == int:
                a[i] += x
                return True
            elif reduceHelper(a[i], x, d):
                return True
    elif d == 1:
        for i in range(len(a)):
            if type(a[i]) == int:
                a[i] += x
                return True
            elif reduceHelper(a[i], x, d):
                return True
    return False

def reduce(a, d=0,s=False):
    if d < 3 and (not s or d == 0):
        for j in range(len(a)):
            if type(a[j]) == list:
                r,y,z = reduce(a[j], d + 1)
                if r:
                    if y != -1:
                        #print("\t"*d,"try place in",a[:j],y, d)
                        for i in range(j-1, -1, -1):
                            if type(a[i]) == int:
                                a[i] += y
                                y = -1
                                break
                            elif reduceHelper(a[i], y, -1):
                                y = -1
                                break
                    if z != -1:
                        for i in range(j+1,len(a)):
                            if type(a[i]) == int:
                                a[i] += z
                                z = -1
                                break
                            elif reduceHelper(a[i], z, 1):
                                z = -1
                                break
                    if d == 0:
                        reduce(a, s=True)
                    return True,y,z
    elif d == 3:
        for j in range(len(a)):
            if type(a[j]) == list:
                #print("\t"*d,"explode ",a[j])
                y,z = a[j]
                for i in range(j-1, -1, -1):
                    if type(a[i]) == int:
                        a[i] += y
                        y = -1
                        break
                    elif reduceHelper(a[i], y, -1):
                        y = -1
                        break
                for i in range(j+1,len(a)):
                    if type(a[i]) == int:
                        a[i] += z
                        z = -1
                        break
                    elif reduceHelper(a[i], z, 1):
                        z = -1
                        break
                a[j] = 0
                return True, y, z

    #split
    if s:
        for i in range(len(a)):
            if type(a[i]) == list:
                r,y,z = reduce(a[i], d + 1, True)
                if r:
                    if d == 0:
                        reduce(a, s=True)
                    return True,-1,-1
            elif a[i] >= 10:
                #print("\t"*d, "split", a[i])
                a[i] = [a[i]//2, math.ceil(a[i]/2)]
                if d == 0:
                    reduce(a, s=True)
                return True,-1,-1
    return False, -1, -1
    

def add(a, b):
    c = [a, b]
    reduce(c, s=True)
    #print("add res",c)
    return c

def magnitude(a):
    if type(a) == int:
        return a
    m = magnitude(a[0]) * 3 + 2 * magnitude(a[len(a) - 1])
    return m
highestMag = 0
for r in range(0,len(rows)):
    for p in range(0,len(rows)):
        if p != r:
            result = add(copy.deepcopy(rows[r]), copy.deepcopy(rows[p]))
            highestMag = max(highestMag, magnitude(result))
print(rows[0])
print("mag",highestMag)