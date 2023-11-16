# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

c = input()
d = deque()

for i in range(int(c)):
    t = input().split(' ')
    if t[0] == 'append':
        d.append(int(t[1]))
    elif t[0] == 'appendleft':
        d.appendleft(int(t[1]))
    elif t[0] == 'pop':
        d.pop()
    elif t[0] == 'popleft':
        d.popleft()
    else:
        print('u dumb?')

for i in d:
    print(i, end=' '
