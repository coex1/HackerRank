from itertools import groupby

groups = []
uniquekeys = []

s = input()

for k, g in groupby(s):
    groups.append(list(g))
    uniquekeys.append(k)

for num, k in enumerate(uniquekeys):
    print(f"({len(groups[num])}, {k})", end=' ')