import numpy as np

N, M = input().split()
N = int(N)
M = int(M)

arr = []
for i in range(N):
    arr.append(input().split())

arr = np.array(arr).astype(np.int64)
sum_arr = np.sum(arr, axis = 0)
print(np.prod(sum_arr))