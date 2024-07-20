from itertools import permutations

word, rep = input().split()

per = list(permutations(word, int(rep)))
for i in sorted(per):
    for j in range(len(i)):
        print(i[j], end='')
    print()