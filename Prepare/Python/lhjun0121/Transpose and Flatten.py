import numpy as np

r, c = map(int, input().split())
arr = []
for _ in range(r):
    arr.append(list(map(int, input().split())))

T = np.transpose(np.array(arr))
F = np.array(arr).flatten()
print(T)
print(F)