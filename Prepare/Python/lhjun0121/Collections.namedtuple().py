from collections import namedtuple

average = 0
N = int(input())
columns_list = input().split()
columns = namedtuple("colums", columns_list)
for _ in range(N):
    average += int(columns(*input().split()).MARKS)
print(average/N)