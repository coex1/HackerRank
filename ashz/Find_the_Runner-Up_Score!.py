if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    first = -100
    second = -100
    for i in arr:
        if i > first:
            second = first
            first = i
        elif i > second and i != first:
            second = i
    print(second)