t = int(input())

for _ in range(t):
    try:
        a, b = map(int, input().split())
        print(int(a/b))
    except ZeroDivisionError:
        print("Error Code: integer division or modulo by zero")
    except ValueError as e:
        print("Error Code:", e)