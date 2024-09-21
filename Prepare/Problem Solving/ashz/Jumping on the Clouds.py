#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    # Write your code here
    
    # current position
    ct = 0
    # jump count
    j = 0
    
    # maximum amount of steps is len(c)
    for i in range(1, len(c)):
        # check the next 2 steps, one will always be safe
        if ct+2 < len(c) and c[ct+2] == 0:
            ct += 2
        else:
            ct += 1
        
        j += 1
        
        # when end of array is reached, end
        if ct == len(c) - 1:
            break
            
    return j

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
