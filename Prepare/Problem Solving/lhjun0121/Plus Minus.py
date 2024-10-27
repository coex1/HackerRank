#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    ratio = [0, 0, 0]
    for i in arr:
        if i > 0:
            ratio[0] += 1
        elif i < 0:
            ratio[1] += 1
        else:
            ratio[2] += 1
    for i in ratio:
        print(round(i/len(arr), 6))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)