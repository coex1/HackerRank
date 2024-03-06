#!/bin/python3

import math
import os
import random
import re
import sys
import collections



if __name__ == '__main__':
    s = input()
    s = list(s)

    counter = [list(i) for i in collections.Counter(s).most_common()]
    
    counter.sort(key = lambda x : (-x[1], ord(x[0])) )
    for i in counter[:3]:
        print(i[0] + " " + str(i[1]))
