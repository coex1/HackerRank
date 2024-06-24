# Enter your code here. Read input from STDIN. Print output to STDOUT
a = int(input())
a_set = set(input().split())
b = int(input())
b_set = set(input().split())

print(len(a_set - b_set))