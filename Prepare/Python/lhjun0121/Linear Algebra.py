import numpy as np

n = int(input())
arr = []
for _ in range(n):
    arr.append(np.array(list(map(float, input().split()))))
print(round(np.linalg.det(arr), 2))