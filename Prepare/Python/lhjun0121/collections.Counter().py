from collections import Counter

n = int(input())

sizes = Counter(list(map(int, input().split())))

customers = int(input())

total = 0

for i in range(customers):
    size, price = map(int, input().split())
    if size in sizes.keys() and sizes[size] > 0:
        sizes[size] -= 1
        total += price

print(total)