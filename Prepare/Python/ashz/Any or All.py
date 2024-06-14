# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
arr = list(map(int, input().split()))

c = all([any(arr), all(arr)])
for i in arr:
    if i < 0:
        c = False
cc = False
for i in arr:
    if str(i) == str(i)[::-1]:
        cc = True
        break

print(c and cc)
