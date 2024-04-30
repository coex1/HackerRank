#!/bin/python3

import math
import os
import random
import re
import sys
import time
from datetime import datetime 

# Complete the time_delta function below.
def time_delta(t1, t2):
    fmt = "%a %d %b %Y %H:%M:%S %z"

    for _ in range(t):

        t1_delta = datetime.strptime(t1, fmt)

        t2_delta = datetime.strptime(t2, fmt)

        diff = (t1_delta - t2_delta).total_seconds()

        return str(int(abs(diff)))
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()