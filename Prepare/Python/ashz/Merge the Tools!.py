def merge_the_tools(string, k):
    # your code goes here
    subcnt = int(len(string)/k)
    substr = []
    nstr = []
 
    p = 0
    for i in range(subcnt):
        t = (i+1)*k
        substr.append(string[p:t])
        p = t
    
    for i in substr:
        tmp = []
        for j in i:
            if not j in tmp:
                tmp.append(j)
        t = ""
        for j in tmp:
            t += j
        nstr.append(t)
    
    for j in nstr:
        print(j)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k
