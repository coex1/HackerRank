if __name__ == '__main__':
    N = int(input())
    Lists = []

    for _ in range(N):
        a = input().split()
        cmd = a[0]
        
        if cmd == 'insert':
            Lists.insert(int(a[1]), int(a[2]))
        elif cmd == 'remove':
            Lists.remove(int(a[1]))
        elif cmd == 'append':
            Lists.append(int(a[1]))
        elif cmd == 'sort':
            Lists.sort()
        elif cmd == 'reverse':
            Lists.reverse()
        elif cmd == 'pop':
            Lists.pop()
        elif cmd == 'print':
            print(Lists)
            Lists = []