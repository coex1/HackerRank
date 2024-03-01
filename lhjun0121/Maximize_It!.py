from itertools import product

K, M = map(int, input().split())

max = 0
sum = 0

_list = []

for _ in range(K):
    sublist = list(map(int, input().split()))
    sublist.pop(0)
    _list.append(sublist)

pdlist = list(product(*_list))

for i in pdlist:
    for j in i:
        sum += j**2

    if sum % M > max:
        max = sum % M

    sum = 0

print(max)