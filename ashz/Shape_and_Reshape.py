import numpy

m = list(map(int, input().split()))

c = numpy.array(m)

print(numpy.reshape(c, (3, 3)))
