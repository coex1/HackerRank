# Enter your code here. Read input from STDIN. Print output to STDOUT
M = int(input())
sM = set(map(int, input().split(' ')))
N = int(input())
sN = set(map(int, input().split(' ')))

d = sM.difference(sN)
d.update(sN.difference(sM))

for i in sorted(d):
    print(i)
