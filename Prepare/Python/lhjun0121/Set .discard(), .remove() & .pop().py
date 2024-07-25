n = int(input())
s = set(map(int, input().split()))

for _ in range(int(input())):
    l = input().rstrip()
    if l == 'pop':
        s.pop()
    else:
        name = l.split()[0]
        elm = int(l.split()[1])
        if name == 'remove':
            
            s.remove(elm)
        if name == 'discard':
            s.discard(elm)
print(sum(s))
