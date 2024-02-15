# Enter your code here. Read input from STDIN. Print output to STDOUT

A_len = int(input())
A = set(input().split(' '))
N = int(input())
S = 0

for _ in range(N):
    op_name, T_len = input().split(' ')
    T = set(input().split(' '))
    
    if op_name == "update":
        A.update(T)
    elif op_name == "intersection_update":
        A.intersection_update(T)
    elif op_name == "difference_update":
        A.difference_update(T)
    elif op_name == "symmetric_difference_update":
        A.symmetric_difference_update(T)
    
for i in A:
    S += int(i)
    
print(S)
