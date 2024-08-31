#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cutTheSticks' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def cutTheSticks(arr):
    # Write your code here
    res = []
    while len(arr) > 0:
        res.append(len(arr))
        
        # get smallest stick
        low = 1000
        for i in arr:
            if i < low:
                low = i
        
        t = []
        for i in range(len(arr)):
            arr[i] = arr[i] - low
            if arr[i] <= 0:
                t.insert(0, i)
        
        for i in t:
            arr.pop(i)
    
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
