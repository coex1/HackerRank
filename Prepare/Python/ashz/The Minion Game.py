def minion_game(string):
    # your code goes here
    v = 0
    c = 0
    vowel = ['A', 'E', 'I', 'O', 'U']
    slist = list(string)
    slen = len(string)
    
    for i in range(slen):
        if slist[i] in vowel:
            v += slen - i
        else:
            c += slen - i
    
    if v > c:
        print('Kevin '+str(v))
    elif c > v:
        print('Stuart '+str(c))
    else:
        print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s
