# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

s = input()

a = re.findall(r'(?<=[B-DF-HJ-NP-TV-Zb-df-hj-np-tv-z])[AEIOUaeiou]{2,}(?=[b-df-hj-np-tv-z])', s)

if len(a) > 0:
    for i in a:
        print(i)
else:
    print('-1')
