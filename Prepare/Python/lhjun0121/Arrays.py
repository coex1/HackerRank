import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    nparray = numpy.array(arr, float)
    return nparray[::-1]

arr = input().strip().split(' ')
result = arrays(arr)
print(result)