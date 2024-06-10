import numpy

N,M = map(int, input().split())

arr = []
for i in range(N):
    t = list(map(int, input().split()))
    arr.append(t)

rn = numpy.array(arr)
print(numpy.transpose(rn))
print(rn.flatten())
