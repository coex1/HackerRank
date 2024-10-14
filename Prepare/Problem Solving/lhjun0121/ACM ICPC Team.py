#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'acmTeam' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY topic as parameter.
#

def acmTeam(topic):
    from itertools import combinations
    # Write your code here
    max_topic = 0
    teams = 0

    # combinations
    comb = []
    for i in combinations(topic, 2):
        comb.append(i)
    
    subjects = []
    # & bits logic
    for i in comb:
        topic = bin(int(i[0], 2) | int(i[1], 2))[2:]
        subjects.append(topic)

    # determine max topic
    for i in subjects:
        if i.count('1') >= max_topic:
            max_topic = i.count('1')

    for i in subjects:
        if i.count('1') == max_topic:
            teams += 1
    
    return max_topic, teams



if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = open('OUTPUT_PATH', 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
