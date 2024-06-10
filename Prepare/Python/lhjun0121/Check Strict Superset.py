A = list(map(int, input().split()))
N = int(input())
output = True

for _ in range(N):
    otherSet = list(map(int, input().split()))
    if (all(i in A for i in otherSet) == False) or (otherSet == A):
        output = False
        break

print(output)