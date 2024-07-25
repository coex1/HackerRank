import numpy as np

m, n = map(int, input().split())

arr = []

for _ in range(m):
    arr.append(list(map(int, input().split())))

print(np.max(np.min(arr, axis = 1), axis = None))