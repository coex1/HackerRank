def minion_game(string):

    slen = len(string)

    vowels = "AEIOU"

    v_score = 0
    c_score = 0

    for i in range(slen):
        if string[i] in vowels:
            v_score += slen - i
        else:
            c_score += slen - i

    if v_score > c_score:
        print("Kevin " + str(v_score))
    elif v_score < c_score:
        print("Stuart " + str(c_score))
    else:
        print("Draw")




if __name__ == '__main__':
    s = input()
    minion_game(s)