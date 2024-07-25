import numpy as np

m, n = map(int, input().split())
arr = []
for _ in range(m):
    arr.append(np.array(list(map(int, input().split()))))

print(np.mean(arr, axis = 1))
print(np.var(arr, axis = 0))
print(round(np.std(arr), 11))