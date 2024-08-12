#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'extraLongFactorials' function below.
#
# The function accepts INTEGER n as parameter.
#

def extraLongFactorials(n):
    # Write your code here
    c = n - 1
    t = n
    for i in range(n):
        if c <= 0:
            break
        t *= c
        c -= 1
    print(t)

if __name__ == '__main__':
    n = int(input().strip())

    extraLongFactorials(n)
