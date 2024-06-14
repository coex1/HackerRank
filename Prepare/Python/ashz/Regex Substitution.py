# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

def ReplaceOperators(m):
    if m.group(0) == '&&':
        return 'and'
    elif m.group(0) == '||':
        return 'or'
    return 'None'

N = int(input())

for _ in range(N):
    s = input()
    print(re.sub(r'(?<=\ )&&(?=\ )|(?<=\ )\|\|(?=\ )', ReplaceOperators, s))
