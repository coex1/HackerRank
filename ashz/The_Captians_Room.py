# Enter your code here. Read input from STDIN. Print output to STDOUT
K = int(input())
arr = map(int, input().split(' '))

t = {}
for i in arr:
    if i in t.keys():
        t[i] = t.get(i)+1
    else:
        t[i] = 1

for i in t.items():
    if i[1] == 1:
        print(i[0])
