import operator

def person_lister(f):
    def inner(people):
        # complete the function
        age = []
        for i in people:
            pos = len(age)
            for j in range(len(age)):
                if int(age[j][2]) > int(i[2]):
                    pos = j
                    break
            age.insert(pos, i)
        r = []
        for i in age:
            r.append(f(i))
        return r
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')
