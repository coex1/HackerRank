a = int(input())
aset = set(map(int, input().split()))
b = int(input())
bset = set(map(int, input().split()))

print(len(aset.symmetric_difference(bset)))