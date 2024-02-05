import re

pat = r'(?<=[^aeiouAEIOU])([aeiouAEIOU]{2,})(?=[^aeiouAEIOU])'

vowel = re.findall(pat, input())

if not vowel:
    print(-1)
else:
    for i in vowel:
        print(i)