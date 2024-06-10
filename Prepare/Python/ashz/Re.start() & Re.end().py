# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

S = input()
k = input()

T = S
m = re.search(k, T)

if m is None:
    print('(-1, -1)')
else:
    while True:
        print('('+str(m.start())+', '+str(m.end()-1)+')')
        T = T[:m.start()] + ' ' + T[m.start()+1:]
        m = re.search(k, T)
        if m is None:
            break
