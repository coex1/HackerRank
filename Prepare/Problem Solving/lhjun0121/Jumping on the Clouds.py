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
    jumps = 0
    pos = 0
    n = len(c)
    
    while pos < n - 1:
        if pos + 2 < n and c[pos + 2] == 0:
            pos += 2
        else:
            pos += 1
        jumps += 1
        
    return jumps




if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = open('OUTPUT_PATH', 'w')
    
    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
