#!/bin/python3
import math
import os
import random
import re
import sys
# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    n = len(c)
    i = 0
    e = 100
    while True:
        r = (i+k)%n
        if c[r] == 1:
            e -= 3
        else:
            e -= 1
        if r == 0:
            break
        i = r
    return e
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    c = list(map(int, input().rstrip().split()))
    result = jumpingOnClouds(c, k)
    fptr.write(str(result) + '\n')
    fptr.close()
