# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

N = int(input())

for _ in range(N):
    s = input()
    if re.match(r'^[7-9][0-9]{9}$', s) is not None:
        print('YES')
    else:
        print('NO')
