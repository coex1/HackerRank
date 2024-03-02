# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
nlist = input().split(' ')
b = int(input())
blist = input().split(' ')

print(len(set(nlist).union(blist)))
