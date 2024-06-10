from collections import deque

n = int(input())
d = deque()
for i in range(n):
    a = input().split()
    if a[0] == 'append':
        d.append(a[1])
    if a[0] == 'pop':
        d.pop()  
    if a[0] == 'appendleft':
        d.appendleft(a[1])
    if a[0] == 'popleft':
        d.popleft()
        
for i in d:
    print(i, end=' ')
