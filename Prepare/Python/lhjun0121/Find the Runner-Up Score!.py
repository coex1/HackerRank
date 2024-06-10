if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    mx = max(arr)
    arrset = set(arr)
    arrset.remove(mx)
    print(max(arrset))