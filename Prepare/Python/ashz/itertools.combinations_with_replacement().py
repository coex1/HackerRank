# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement

_input = input().split(' ')
S = sorted(_input[0])
k = int(_input[1])

arr = []
for i in combinations_with_replacement(S, k):
    print(''.join(i))
