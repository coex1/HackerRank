# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())

for _ in range(T):
    UID = input()
    
    # check uppercase and digit and repeating character
    u = 0
    d = 0
    s = set()
    r = False
    for i in UID:
        if i.isupper():
            u += 1
        if i.isdigit():
            d += 1
        if i not in s:
            s.add(i)
        else:
            r = True
            break

    if UID.isalnum() and u >= 2 and d >= 3 and len(UID) == 10 and r is False:
        print('Valid')
    else:
        print('Invalid')
