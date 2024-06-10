def count_substring(string, sub_string):
    output = 0
    for i in range(len(string)):
        if string[i] == sub_string[0] and i < (len(string)-len(sub_string)+1):
            cnt = 0
            ii = i
            for j in range(len(sub_string)):
                if string[ii] == sub_string[j]:
                    cnt+=1
                    ii+=1
                    if cnt == len(sub_string):
                        output+=1
    return output

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)