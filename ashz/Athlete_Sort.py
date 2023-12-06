#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    k = int(input())
    
    t = []
    for i in range(n):
        small = 0
        for j in range(0, n-i):
            if arr[j][k] < arr[small][k]:
                small = j
        t.append(arr[small])
        arr.pop(small)
        
    for i in range(n):
        for j in range(m):
            print(t[i][j], end=' ')
        print(''
