import re

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

text=''
for i in range(m):
    for j in range(n):
        text+=(matrix[j][i])

result = re.sub(r'([a-zA-Z]+)([^a-zA-Z]+)([a-zA-Z]+)', r'\1 \3', text)
result = re.sub(r'([a-zA-Z])([^a-zA-Z])([a-zA-Z])', r'\1 \3', result)
print(result)
