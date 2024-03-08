cube = lambda x: x * x * x

def fibonacci(n):
    # return a list of fibonacci numbers
    if n == 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        arr = [0, 1]
        idx = 1
        for _ in range(2, n):
            arr.append(arr[idx] + arr[idx-1])
            idx += 1
        return arr

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n)))
