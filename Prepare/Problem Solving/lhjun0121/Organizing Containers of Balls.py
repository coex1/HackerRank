#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'organizingContainers' function below.
#
# The function is expected to return a STRING.
# The function accepts 2D_INTEGER_ARRAY container as parameter.
#

def organizingContainers(container):
    # Write your code here
    CntContainer = []
    CntColor = []

    for i in range(n):
        CntContainer.append(sum(container[i]))
        s = 0
        for j in range(n):
            s += container[j][i]
        
        CntColor.append(s)
    
    sorted(CntContainer)
    sorted(CntColor)

    for i in range(n):
        if CntColor[i] == CntContainer[i]:
            return "Possible"
        return "Impossible"

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = open('OUTPUT_PATH', 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        fptr.write(result + '\n')

    fptr.close()
