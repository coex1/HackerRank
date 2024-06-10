# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

K, M = map(int, input().split(' '))

_list = []
_k_list = []
_big = 0
_index_sum = 0

for _ in range(K):
    T = list(map(int, input().split(' ')))
    _index_sum += T.pop(0)
    _list.append(T)
    _k_list.append(0)

p = product(*_list)

# loop for the amount of cases we have
#for _ in range(K * _index_sum):
#    _sum = 0
#    for i in range(K):
#        N = _list[i][_k_list[i]]
#        _sum += N * N
#    
#    _rem = _sum % M
#    if _rem > _big:
#        _big = _rem
#     
#    for i in range(K):
#        _k_list[i] += 1
#        if _k_list[i] >= len(_list[i]):
#            _k_list[i] = 0
#        else:
#            break

for i in p:
    _sum = 0
    for j in i:
        _sum += j**2
    
    T = _sum % M
    if T > _big:
        _big = T
 
print(_big
