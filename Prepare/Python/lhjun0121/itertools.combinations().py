from itertools import combinations

S, N = input().split()
s = sorted(S)

for i in range(int(N)):
    ss = list(combinations(s, int(i + 1)))
    for j in ss:
        print("".join(j))
