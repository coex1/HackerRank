#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
    # Write your code here
    
    length = 0
    
    # an array to hold the remainders
    rem = [0] * k
    for i in s:
        rem[i % k] += 1
    
    # at most, only 1 number in the subset can be perfectly divisable by 'k'
    length += min(rem[0], 1)
    
    # if 'k' is even, count only 1 of it's 'k/2' remainders
    if k % 2 == 0:
        length += min(rem[k//2], 1) # if not floor division, runtime error could occur. why?
    
    # other odd cases
    for i in range(1, (k//2)+1):
        # prevent over-counting
        if i != k - i:
            length += max(rem[i], rem[k-i])

    return length

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()
