# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

S = input()

pattern = re.compile(r'([a-zA-Z0-9])\1')
match = pattern.search(S)
if match:
    print(match.group(1))
else:
    print(-1)
