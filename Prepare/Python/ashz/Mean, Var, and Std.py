import numpy
N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
narr = numpy.array(arr)
print(numpy.mean(narr, axis=1))
print(numpy.var(narr, axis=0))
print(round(numpy.std(narr), 11))
