n = int(input())

arr = {}
for i in range(n):
    word = input()
    if word in arr:
        arr[word]+=1
    else:
        arr[word] = 1

print(len(arr))
for i in arr.keys():
    print(arr[i], end=" ")