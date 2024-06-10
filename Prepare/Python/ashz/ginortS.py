# Enter your code here. Read input from STDIN. Print output to STDOUT
# lower > upper > odd > even
S = input()
lower = ''
upper = ''
odd = ''
even = ''

for i in S:
    if i.islower():
        lower += i
    elif i.isupper():
        upper += i
    elif i.isnumeric():
        if int(i) % 2 == 0:
            even += i
        else:
            odd += i

c = ''
c += ''.join(sorted(lower))
c += ''.join(sorted(upper))
c += ''.join(sorted(odd))
c += ''.join(sorted(even))

print(c)
