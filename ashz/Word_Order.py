# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())

s = {}
for _ in range(n):
    a = input()
    if a in s.keys():
        s[a] += 1
    else:
        s[a] = 1

print(len(s.keys()))
for i in s.keys():
    print(s[i], end=" ")
