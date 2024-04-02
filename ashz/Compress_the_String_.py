# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools

S = input()

for i, j in itertools.groupby(S, key=None):
    c = 0
    for k in j:
        c += 1
    print('('+str(c)+', '+str(i)+')', end=' ')
