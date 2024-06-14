# Enter your code here. Read input from STDIN. Print output to STDOUT
N, X = map(int, input().split())

arr = []

for _ in range(X):
    arr.append(list(map(float, input().split())))

for i in zip(*arr):
    _sum = 0
    for j in i:
        _sum += j
    
    print(_sum/X)
