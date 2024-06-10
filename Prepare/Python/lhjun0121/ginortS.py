s = input()

uppers = []
lowers = []
odds = []
evens = []

for i in s:
    if i.isdigit():
        if int(i) % 2  != 0:
            odds.append(i)
        else:
            evens.append(i)

    else:
        if i.isupper():
            uppers.append(i)
        else:
            lowers.append(i)

S = ''.join(sorted(lowers)) + ''.join(sorted(uppers)) + ''.join(sorted(odds)) + ''.join(sorted(evens))
print(S)