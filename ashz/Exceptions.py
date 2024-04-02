# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())
for _ in range(T):
    a, b = input().split(' ')
    try:
        c = int(a)/int(b)
        print(int(c))
    except ValueError as e:
        print('Error Code: '+str(e))
    except ZeroDivisionError as e:
        print('Error Code: integer division or modulo by zero')
