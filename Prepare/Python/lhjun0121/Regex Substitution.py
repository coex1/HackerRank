import re

def symbols(html):
    html = re.sub(r'(?<=\s)&&(?=\s)', 'and', html)
    html = re.sub(r'(?<=\s)\|\|(?=\s)', 'or', html)
    return print(html)

html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'

symbols(html)