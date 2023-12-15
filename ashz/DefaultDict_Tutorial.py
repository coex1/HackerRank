# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

n,m = map(int,input().split(' '))

A = []
B = []
for _ in range(n):
    A.append(input())
for _ in range(m):
    B.append(input())
    
d = defaultdict(list)

for i in B:
    if len(d[i]) != 0:
        continue
    for j in range(n):
        if A[j] == i:
            d[i].append(j+1)

for i in B:
    if len(d[i]) == 0:
        print('-1')
    else:
        for j in d[i]:
            print(j, end=' ')
        print(''
