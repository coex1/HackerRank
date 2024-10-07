#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'queensAttack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER r_q
#  4. INTEGER c_q
#  5. 2D_INTEGER_ARRAY obstacles
#

def queensAttack(n, k, r_q, c_q, obstacles):
    # Write your code here
    top = r_q - 1
    bottom = n - r_q
    left = c_q - 1
    right = n - c_q

    topleft = min(top, left)
    topright = min(top, right)
    bottomleft = min(bottom, left)
    bottomright = min(bottom, right)
    
    for i in obstacles:
        if r_q == i[0]:
            if i[1] > c_q:
                right = min(right, (i[1] - c_q - 1))
            else:
                left = min(left, (c_q - i[1] -1))
        if c_q == i[1]:
            if i[0] > r_q:
                bottom = min(bottom, (i[0] - r_q - 1))
            else:
                top = min(top, (r_q - i[0] - 1))

        if abs(i[0] - r_q) == abs(i[1] - c_q):
            if i[0] < r_q and i[1] < c_q:
                topleft = min(topleft, abs(i[0] - r_q) - 1)
            elif i[0] < r_q and i[1] > c_q:
                topright = min(topright, abs(i[0] - r_q) - 1)
            elif i[0] > r_q and i[1] < c_q:
                bottomleft = min(bottomleft, abs(i[0] - r_q) - 1)
            else:
                bottomright = min(bottomright, abs(i[0] - r_q) - 1)

    return top + bottom + left + right + topleft + topright + bottomleft + bottomright

if __name__ == '__main__':
    fptr = open('OUTPUT_PATH', 'w')
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    r_q = int(second_multiple_input[0])

    c_q = int(second_multiple_input[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
