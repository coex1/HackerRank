from itertools import product

A = list(map(int, input().split()))
B = list(map(int, input().split()))

plist = list(product(A, B))
for i in plist:
    print(i, end = " ")