def count_substring(string, sub_string):
    cnt = 0
    sl = len(string)
    for i in range(sl):
        flag = True
        c = 0
        for j in sub_string:
            if int(i)+c >= sl:
                flag = False
                break
            if string[int(i)+c] != j:
                flag = False
                break
            c += 1
        if flag:
            cnt += 1
    return cnt

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count
