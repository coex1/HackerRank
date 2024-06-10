anum = int(input())
A = set(map(int, input().split()))

N = int(input())

for _ in range(N):
    a, b = input().split()
    if a == "intersection_update":
        otherset = set(map(int, input().split()))
        A.intersection_update(otherset)
    elif a == "update":
        otherset = set(map(int, input().split()))
        A.update(otherset)
    elif a == "symmetric_difference_update":
        otherset = set(map(int, input().split()))
        A.symmetric_difference_update(otherset)
    elif a == "difference_update":
        otherset = set(map(int, input().split()))
        A.difference_update(otherset)

print(sum(A))