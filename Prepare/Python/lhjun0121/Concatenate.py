import numpy as np

N, M, P = map(int, input().split())
Nlist = []
Mlist = []

for _ in range(N):
    Nlist.append(list(map(int, input().split())))
for _ in range(M):
    Mlist.append(list(map(int, input().split())))

con = np.concatenate((np.array(Nlist), np.array(Mlist)))
print(con)