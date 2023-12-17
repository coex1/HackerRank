from collections import defaultdict

a, b = map(int, input().split())

d = defaultdict(list)

for i in range(a):
    d[input()].append(str(i+1))
for i in range(b):
    bb = input()
    if bb in d:
        print(' '.join(d[bb]))
    else:
        print(-1)