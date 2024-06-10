from itertools import combinations_with_replacement

S, n = input().split()
S = sorted(S)

for i in combinations_with_replacement(S, int(n)):
    print("".join(i))