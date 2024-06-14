import numpy
N = int(input())
A = []
B = []
for _ in range(N):
    A.append(list(map(int, input().split())))
for _ in range(N):
    B.append(list(map(int, input().split())))
AA = numpy.array(A)
BB = numpy.array(B)
D = numpy.dot(AA, BB)
print(D)
