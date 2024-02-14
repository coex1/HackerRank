if __name__ == '__main__':
    NL = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        T = [name, float(score)]
        NL.append(T)
    
    # find the second lowest score number
    lowest = None
    sec_lowest = None
    for i in NL:
        # debug
        # print('---> ' + str(lowest) + ' / ' + str(sec_lowest))
        if lowest is None:
            lowest = i[1]
            continue
        if i[1] < lowest:
            sec_lowest = lowest
            lowest = i[1]
            continue
        if i[1] == lowest:
            continue
        if sec_lowest is None:
            sec_lowest = i[1]
            continue
        if i[1] < sec_lowest:
            sec_lowest = i[1]

    # list of second lowest score student names
    names = []
    for i in NL:
        if i[1] == sec_lowest:
            names.append(i[0])
    
    names.sort()
    for i in names:
        print(i)
