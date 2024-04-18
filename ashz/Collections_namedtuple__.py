# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple

N = int(input())
columns = input()

Student = namedtuple('Student', columns)
arr = []

for _ in range(N):
    arr.append(Student(*input().split()))

_sum = 0
for i in arr:
    _sum += int(i.MARKS)

print(float(_sum/len(arr)))
