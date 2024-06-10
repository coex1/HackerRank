# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
nlist = set(input().split(' '))
f = int(input())
flist = set(input().split(' '))

print(len(nlist.intersection(flist)))
