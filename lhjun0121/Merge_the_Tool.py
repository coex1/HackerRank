def merge_the_tools(string, k):
    # your code goes here
    string = list(string)

    mul = int(len(string)/k)

    for j in range(mul):

        line=[]

        for i in range(k):
            if string[i + j*k] not in line:
                line.append(string[i + j*k])

        for i in line:
            print(i, end='')
            
        print()

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)