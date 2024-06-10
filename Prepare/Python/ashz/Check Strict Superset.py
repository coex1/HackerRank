# Enter your code here. Read input from STDIN. Print output to STDOUT

A = input().split()
N = int(input())
T = []

for _ in range(N):
    T.append(input().split())

isSuper = True
for i in T:
    t = -1
    if len(A) <= len(i):
        isSuper = False
        break
    for j in range(len(i)):
        if not (i[j] in A):
            isSuper = False
            break
    if not isSuper:
        break
            
if isSuper:
    print('True')
else:
    print('False')
