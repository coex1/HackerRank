# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

N = int(input())

for _ in range(N):
    s = input().split()
    if re.match(r'<[A-Za-z][A-z0-9-._]*@[A-Za-z]*\.[A-Za-z]{1,3}>', s[1]) is not None:
        print(s[0], s[1])
