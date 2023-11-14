def print_rangoli(size):
    Size = 2*size-1
    for i in range(Size):
        line=""
        if i < size:
            for j in range(96+size, 95+size-i,-1):
                line += chr(j)
            for j in range(97+size-i,97+size):
                line += chr(j)
            line = "-".join(line.center(Size, "-"))
            print(line)
        #size >= i
        else:
            for j in range(96 + size, 97 - size + i,-1):
                line += chr(j)
            for j in range(99 - size + i, 97 + size ,1):
                line += chr(j)
            line = "-".join(line.center(Size, "-"))
            print(line)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
