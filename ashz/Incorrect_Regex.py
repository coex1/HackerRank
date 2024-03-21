# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

T = int(input())

for _ in range(T):
    s = input()
    
    if s.endswith('+') and not s.endswith('\\+') and not s.endswith(']+'):
        print('False')
        continue

    try:
        re.match(s, 'hello')
        print('True')
    except Exception or re.error:
        print('False')
