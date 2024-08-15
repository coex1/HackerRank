#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'appendAndDelete' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#  3. INTEGER k
#

def appendAndDelete(s, t, k):
    # Write your code here
    if len(t) > len(s):
        temp = t
        t = s
        s = temp

    i = 0
    while s[i] == t[i]:
        i += 1
        if i == len(t):
            break

    s2 = s[i:]
    t2 = t[i:]

    if s == t:
        return "Yes"
    elif t in s:
        return "Yes" if (k >= len(s2) and (k-len(s2)) % 2 == 0) or k >= len(s) + len(t) else "No"
    else:
        return "Yes" if k >= len(s2) + len(t2) else "No"


if __name__ == '__main__':
    fptr = open('output.txt', 'w')
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input().strip())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
