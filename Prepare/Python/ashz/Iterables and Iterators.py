# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

N = int(input())
_list = input().split(' ')
K = int(input())

c_len = 0
c_valid = 0

for i in combinations(_list, K):
    c_len += 1
    if 'a' in i:
        c_valid += 1

print(float(c_valid/c_len))
