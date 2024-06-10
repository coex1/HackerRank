#!/bin/python3

import math
import os
import random
import re
import sys
import time
from datetime import datetime as d

# Complete the time_delta function below.
def time_delta(t1, t2):
    t1a = t1.split(' ')
    t2a = t2.split(' ')
    t1s = 0
    t2s = 0
    
    s = ""+t1a[3]+"/"+t1a[2]+"/"+t1a[1]+" "+t1a[4]
    t1s += int(d.timestamp(d.strptime(s, "%Y/%b/%d %H:%M:%S")))
 
    z = t1a[5]
    t = ((int(z[1])*10 + int(z[2])) * 3600) + ((int(z[3])*10 + int(z[4])) * 60)
    if z[0] == '+':
        t *= -1
    t1s += t
    
    s = ""+t2a[3]+"/"+t2a[2]+"/"+t2a[1]+" "+t2a[4]
    t2s += int(d.timestamp(d.strptime(s, "%Y/%b/%d %H:%M:%S")))
    
    z = t2a[5]
    t = ((int(z[1])*10 + int(z[2])) * 3600) + ((int(z[3])*10 + int(z[4])) * 60)
    if z[0] == '+':
        t *= -1
    t2s += t
    
    k = t1s - t2s
    if k < 0:
        k *= -1

    return str(k)
 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()

