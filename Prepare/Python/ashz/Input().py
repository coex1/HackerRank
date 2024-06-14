# Enter your code here. Read input from STDIN. Print output to STDOUT
x, k = map(int, input().split())

a = input()
if eval(a) == k:
    print('True')
else:
    print('False')
