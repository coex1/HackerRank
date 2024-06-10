import re

def validating(card_number):
    a = card_number.replace('-', '')

    if not re.match(r'^\d{16}$', a):
        return 'Invalid'
    
    if not re.match(r'^[456]', a):
        return 'Invalid'
    
    if re.search(r'(\d)\1{3,}', a):
        return 'Invalid'
    
    if '-' in card_number:
        if not re.match(r'^(\d{4}-){3}\d{4}$', card_number):
            return 'Invalid'
    
    return 'Valid'

n = int(input().strip())
numbers = [input().strip() for _ in range(n)]

results = [validating(n) for n in numbers]

for r in results:
    print(r)