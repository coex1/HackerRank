from itertools import combinations

N = int(input())

_str = input().split()

K = int(input())

contain = 0
length = 0

for i in combinations(_str, K):
    if 'a' in i:
        contain += 1
    length += 1

print(round(contain/length, 4))