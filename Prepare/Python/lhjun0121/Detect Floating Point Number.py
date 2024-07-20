import re

n = int(input()) 

for i in range(n):
    pattern = re.match(r'[+-]?\d*\.\d+$', input())
    if pattern == None:
        print(False)
    else:
        print(True)