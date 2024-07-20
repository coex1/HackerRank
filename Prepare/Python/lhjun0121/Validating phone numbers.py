import re

n = int(input())
for _ in range(n):
    pattern = re.match(r'[7-9]\d{9}$', input())
    if pattern:
        print("YES")
    else:
        print("NO")