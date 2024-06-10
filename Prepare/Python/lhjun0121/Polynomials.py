import numpy

coef = list(map(float, input().split()))

x = float(input())

result = numpy.polyval(coef, x)

print(result)
