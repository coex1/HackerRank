# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

def isValid(card):
    if re.fullmatch(r'[456][0-9]{3}-[0-9]{4}-[0-9]{4}-[0-9]{4}', card) is not None or re.fullmatch(r'[456][0-9]{15}', card) is not None:
        v = card[0]
        c = 1
        for i in range(1, len(card)):
            if card[i] == '-':
                continue
            if v == card[i]:
                c+=1
                if c >= 4:
                    return False
            else:
                v = card[i]
                c = 1
    else:
        return False
    
    return True

N = int(input())

for _ in range(N):
    card = input()
    if isValid(card):
        print('Valid')
    else:
        print('Invalid')
