# Enter your code here. Read input from STDIN. Print output to STDOUT
list_len, set_len  = input().split()
list_len = int(list_len)
set_len = int(set_len)
arr = list(map(int, input().split()))
set1 = set(map(int, input().split()))
set2 = set(map(int, input().split()))

point = 0

for i in arr:
    if i in set1:
        point+=1
    elif i in set2:
        point-=1

print(point)