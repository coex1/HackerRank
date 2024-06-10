cube = lambda x : x**3

def fibonacci(n):
    fib = []
    for i in range(0, n):
        if i < 2:
            fib.append(i)
        if i == 2:
            fib.append(1)
        if i > 2:
            fib.append(fib[i-2] + fib[i-1])
    
    return fib
        

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))