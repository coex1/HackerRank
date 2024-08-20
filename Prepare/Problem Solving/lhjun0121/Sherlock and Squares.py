#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'squares' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER b
#

def squares(a, b):
    # Write your code here
    starting = math.ceil(math.sqrt(a))
    ending = math.ceil(math.sqrt(b))
    if ending == math.sqrt(b):
        return ending - starting + 1
    else:
        return ending - starting


if __name__ == '__main__':
    fptr = open('OUTPUT_PATH.txt', 'w')
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
