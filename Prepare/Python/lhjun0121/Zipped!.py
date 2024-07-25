m, n = map(int, input().split())

score = []
for _ in range(n):
    score.append(list(map(float, input().split())))

for i in zip(*score):
    print(sum(i) / n)