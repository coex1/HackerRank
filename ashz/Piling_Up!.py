# Enter your code here. Read input from STDIN. Print output to STDOUT
TestCase = int(input())

for _ in range(TestCase):
    cube_cnt = int(input())
    cubes = list(map(int, input().split(' ')))
    flag = True
    bottom = 0
    first = True
    
    for _ in range(len(cubes)):
        target_idx = 0
        if cubes[0] > cubes[len(cubes)-1]:
            target_idx = 0
        else:
            target_idx = len(cubes)-1
        
        if cubes[target_idx] <= bottom or first:
            first = False
            bottom = cubes[target_idx]
            cubes.pop(target_idx)
        else:
            flag = False
            break
    if flag:
        print('Yes')
    else:
        print('No'
