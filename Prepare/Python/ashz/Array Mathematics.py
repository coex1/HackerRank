import numpy
N, M = map(int, input().split())
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))
B = []
for _ in range(N):
    B.append(list(map(int, input().split())))

AA = numpy.array(A)
BB = numpy.array(B)
print(numpy.add(AA, BB))
print(numpy.subtract(AA, BB))
print(numpy.multiply(AA, BB))
print(numpy.floor_divide(AA, BB))
print(numpy.mod(AA, BB))
print(numpy.power(AA, BB))
