# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

def doesBracketCountMatch(s):
    start = 0
    end = 0
    for i in s:
        if i == '<':
            start += 1
        elif i == '>':
            end += 1
    
    if start == end:
        return True
    else:
        return False

N = int(input())
code = []

for _ in range(N):
    S = input()
    code.append(S)

cleanCode = []
T = ''

# combine strings till a full tag is made
for i in code:
    T = T+i
    if doesBracketCountMatch(T):
        cleanCode.append(T)
        T = ''

for i in cleanCode:
    M = re.findall(r'(?:<!--.*?-->)|(<([^\s/][^>]*)>)', i)
    for j in M:
        #print(j)
        if len(j[1]) > 0:
            arr = list(j[1].split(' '))
            if len(arr) == 1:
                print(arr[0])
            else:
                print(arr[0])
                #newMatch = re.findall(r'\w+="[^"]+"', j[1])
                newMatch = re.findall(r'[\w-]+\s*=\s*"[^"]+"', j[1])
                #print(newMatch)
                for k in newMatch:
                    cleanText = k.strip().split('=', 1)
                    #print(cleanText)
                    name = cleanText[0]
                    tmp = re.findall(r'"([^"]*)"', cleanText[1])
                    if len(tmp) > 0:
                        value = tmp[0]
                    else:
                        continue
                    print('-> ' + name + ' > ' + value)
