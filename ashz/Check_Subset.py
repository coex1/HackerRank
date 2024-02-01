# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())

for _ in range(T):
    Ac = int(input())
    A = input().split(' ')
    Bc = int(input())
    B = input().split(' ')
    check = True
    for i in A:
        if not (i in B):
            check = False
            break
    if check:
        print('True')
    else:
        print('False')
