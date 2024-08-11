#!/bin/python3

import math
import os
import random
import re
import sys

def lcm(a, b):
    return int(a*b / math.gcd(a,b))

def jumpingOnClouds(c, k):
    e = 100
    if lcm(n, k) == n:
        for i in range(0, len(c), k):
            e -= 1
            if c[i] == 1:
                e -= 2
    else:
        c = c*int(lcm(n, k)/n)
        for i in range(0, len(c), k):
            e -= 1
            if c[i] == 1:
                e -= 2
    return e

if __name__ == '__main__':
    fptr = open('output.txt', 'w')
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
