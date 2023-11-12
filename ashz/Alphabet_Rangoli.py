def print_rangoli(size):
    # your code goes here
    x = ((size-1)*2)+1
    y = size
    cur = 0
    
    for i in range(y):
        cur = size-1
        for j in range(size-1-i):
            print('--', end="")
        for j in range(i):
            print(chr(97+cur)+"-", end="")
            cur -= 1
                
        print(chr(97+cur), end="")
        cur += 1
        
        for j in range(i):
            print("-"+chr(97+cur), end="")
            cur += 1
        for j in range(size-1-i):
            print('--', end="")
        print("")
    
    for i in range(y-1):
        cur = size-1
        for j in range(i+1):
            print('--', end="")
        for j in range(size-2-i):
            print(chr(97+cur)+"-", end="")
            cur -= 1
        
        print(chr(97+cur), end="")
        cur += 1
        
        for j in range(size-2-i):
            print("-"+chr(97+cur), end="")
            cur += 1
        for j in range(i+1):
            print('--', end="")
        print("")

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
