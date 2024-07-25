import re

n = int(input())
for _ in range(n):
    string = input()
    digit = re.sub(r'[^0-9]', '', string)
    alpha = re.sub(r'[^a-zA-Z]', '', string)
    if len(digit) >= 3 and len(alpha) >= 2 and len(string) == 10 and \
        len(digit) == len(set(digit)) and len(alpha) == len(set(alpha)):
        print("Valid")
    else:
        print("Invalid")