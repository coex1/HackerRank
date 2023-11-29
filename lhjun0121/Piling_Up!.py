T = int(input())

output=[]   # Yes / No

for i in range(T):
    size = int(input())
    arr = list(map(int, input().split()))

    queue=[] # pick order

    if arr[0] >= arr[size-1]:
        queue.append(arr.pop(0))
        size -= 1
    else:
        queue.append(arr.pop(size-1))
        size -= 1

    nsize = size
    for j in range(size):
        if arr[0] >= arr[nsize-1] and arr[0] <= queue[-1]:
            queue.append(arr.pop(0))
            nsize -= 1
        elif arr[nsize-1] >= arr[0] and arr[nsize-1] <= queue[-1]:
            queue.append(arr.pop(nsize-1))
            nsize -= 1
        else:
            break
    
    if nsize > 0:
        output.append("No")
    else:
        output.append("Yes")

for i in output:
    print(i)