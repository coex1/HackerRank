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
    same_cnt = 0
    move = k
 
    # find the position where the strings are the same
    for i in range(len(s)):
        if i >= len(t):
            break
        if s[i] == t[i]:
            same_cnt += 1
        else:
            break
 
    # delete 1
    change = len(s) - same_cnt
    move = move - change

    # check 1
    if move < 0:
        print(1)
        return "No"
    elif move == 0:
        if s[:same_cnt] == t:
            print(2)
            return "Yes"
        else:
            print(3)
            return "No"

    # append 1
    change = len(t) - same_cnt
    move = move - change

    # check 2 (assume string is the same at this point)
    if move < 0:
        print(4)
        return "No"
    elif move == 0:
        return "Yes"

    # check 3 (we have moves left)
    if move % 2 == 0:
        print(5)
        return "Yes" # go back and forth evenly
    if move > same_cnt * 2:
        print(6)
        return "Yes" # can go back and forth, and delete extras
    else:
        print(7)
        return "No"
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input().strip())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()

