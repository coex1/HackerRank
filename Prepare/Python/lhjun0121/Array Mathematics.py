import numpy as np

n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(np.array(list(map(int, input().split()))))
b = []
for i in range(n):
    b.append(np.array(list(map(int, input().split()))))
    
print(np.reshape((np.add(a,b)), (n,m)))
print(np.reshape((np.subtract(a,b)), (n,m)))
print(np.reshape((np.multiply(a,b)), (n,m)))
print(np.reshape((np.floor_divide(a,b)), (n,m)))
print(np.reshape((np.mod(a,b)), (n,m)))
print(np.reshape((np.power(a,b)), (n,m)))