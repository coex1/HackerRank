import numpy
N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(float, input().split())))
print(round(numpy.linalg.det(arr), 2))
