t = int(input())

for _ in range(t):
    Anum = int(input())
    Aset = set(map(int, input().split()))

    Bnum = int(input())
    Bset = set(map(int, input().split()))
    if Aset & Bset == Aset:
        print(True)
    else: print(False)