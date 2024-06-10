import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    n = numpy.array(arr[::-1], float)
    return n

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
