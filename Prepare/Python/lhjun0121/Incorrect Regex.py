import re

patterns = []

results = []

N = int(input())

for _ in range(N):
    patterns.append(input())

for pattern in patterns:
    try:
        re.compile(pattern)
        results.append(True)
    except re.error:
        results.append(False)

for i in results:
    print(i)