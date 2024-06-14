# Enter your code here. Read input from STDIN. Print output to STDOUT
EN = int(input())
EN_S = set(input().split())
FR = int(input())
FR_S = set(input().split())

print(len(EN_S.symmetric_difference(FR_S)))
