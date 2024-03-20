# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

n = int(input())

arr = OrderedDict()

for _ in range(n):
    s = input().split(' ')
    price = int(s[len(s)-1])
    s.pop(len(s)-1)
    name = ""
    for i in s:
        name = name + i + " "
        
    if name not in list(arr):
        arr[name] = price
    else:
        arr[name] += price
   
for i in list(arr):
    print(str(i) + str(arr[i]))
