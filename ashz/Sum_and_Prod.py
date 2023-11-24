import numpy

a,b = map(int, input().split())
t = []
for i in range(a):
    t.append(list(map(int, input().split())))

print(numpy.prod(numpy.sum(t, axis=0))
