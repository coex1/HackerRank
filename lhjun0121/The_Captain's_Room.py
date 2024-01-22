k = int(input())

numlist = list(map(int, input().split()))

sumlist = sum(numlist)
set_sumlist = sum(set(numlist))

output = (set_sumlist * k - sumlist) / (k - 1)

print(int(output))