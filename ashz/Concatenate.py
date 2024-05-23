import numpy

N,M,P = map(int, input().split())

arr1 = []
arr2 = []

for _ in range(N):
    t = list(map(int, input().split()))
    arr1.append(t)

for _ in range(M):
    t = list(map(int, input().split()))
    arr2.append(t)

na1 = numpy.array(arr1)
na2 = numpy.array(arr2)

print(numpy.concatenate((na1, na2), axis = 0))
