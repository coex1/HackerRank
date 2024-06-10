M = int(input())

a = set(map(int, input().split()))

N = int(input())

b = set(map(int, input().split()))

outputs = a.union(b) - a.intersection(b)
for i in sorted(outputs):
    print(i)