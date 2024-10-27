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
    
    container_sizes = [sum(row) for row in container]
    ball_counts = [sum(i) for i in zip(*container)]
    return "Possible" if sorted(container_sizes) == sorted(ball_counts) else "Impossible"
    
    new_map = {}
    for i in container:
        for j in i:
            if new_map.get(str(j)) is not None:
                new_map[str(j)] = new_map[str(j)] + 1
            else:
                new_map[str(j)] = 1
                print('--------> ' + str(j))
    
    print(new_map) 
    
    _l = True
    _len = -1
    for i in new_map.values():
        print('---> ' + str(i))
        if _len < 0:
            _len = i
            continue
        if i != _len:
            _l = False
            break
    
    print('')
    
    if _l:
        return "Possible"
    else:
        return "Impossible"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        fptr.write(result + '\n')

    fptr.close()
