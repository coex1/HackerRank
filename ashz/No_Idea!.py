# Enter your code here. Read input from STDIN. Print output to STDOUT
a, b = input().split(' ')

arr = map(int, input().split(' '))
like = set(map(int, input().split(' ')))
hate = set(map(int, input().split(' ')))

happiness = 0

for i in arr:
    if i in like:
        happiness += 1
    elif i in hate:
        happiness -= 1

print(happiness)
