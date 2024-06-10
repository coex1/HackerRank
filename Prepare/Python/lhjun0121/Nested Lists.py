if __name__ == '__main__':
    st = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        st.append([name, score])

    st.sort(key=lambda x : (-x[1], x[0]))
    min = st[-1][1]
    for i in reversed(st):
        if i[1] == min:
            st.pop()
        else:
            break

    output=[]
    secmin = st[-1][1]
    for i in reversed(st):
        if i[1] == secmin:
            output.append(i[0])
        else:
            break
    
    for i in reversed(output):
        print(i)
