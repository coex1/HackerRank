# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
S = input().split(' ')
_s = sorted(S[0])

for j in range(1, int(S[1])+1):
    for i in combinations(_s, j):
        print(''.join(i))
