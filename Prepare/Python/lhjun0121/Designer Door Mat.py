h, w = map(int, input().split())

for i in range(1, h // 2 + 1):
    dot = '.|.' * (i * 2 - 1)
    print(dot.center(w, '-'))

print("WELCOME".center(w, '-'))

for i in range(h // 2, 0, -1):
    dot = '.|.' * (i * 2 - 1)
    print(dot.center(w, '-'))