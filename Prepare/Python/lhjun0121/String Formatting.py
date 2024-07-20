def print_formatted(number):
    # your code goes here
    l = len(str(bin(number)[2:]))
    for i in range(1, number + 1):
        print(format(i).rjust(l), format(i, 'o').rjust(l), format(i, 'X').rjust(l), format(i, 'b').rjust(l))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)