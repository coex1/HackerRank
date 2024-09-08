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
    from collections import Counter
    # Write your code here
    length = 0

    s = [i % k for i in s]
    count = Counter(s)

    if count[0] > 0:
        length += 1

    for i in range(1, (k // 2) + 1):
        if i != k - i:
            length += max(count[i], count[k - i])
    
    if k % 2 == 0 and count[k // 2] > 0:
        length += 1

    return length


if __name__ == '__main__':
    fptr = open('OUTPUT_PATH.txt', 'w')
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()
