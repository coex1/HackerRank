# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

T = int(input())

for _ in range(T):
    s = input()
    if re.match(r'[+-]{0,1}[0-9]*\.[0-9]+$', s) is not None:
        print('True')
    else:
        print('False')
