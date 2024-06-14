def wrapper(f):
    def fun(l):
        # complete the function
        for i in range(len(l)):
            number = l[i]
            skip = len(number)-10
            s = ""
            cnt = 0
        
            for j in range(skip, len(number)):
                s += number[j]
                cnt += 1
                if cnt == 5:
                    s += " "
            s = "+91 " + s
            l[i] = s
        f(l)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 



