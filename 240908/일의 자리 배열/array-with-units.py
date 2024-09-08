a1,a2 = tuple(map(int, input().split()))
arr = [0]*11
arr[1],arr[2] = a1,a2
for i in range(3,11):
    arr[i] = arr[i-1]+arr[i-2]
    if arr[i] >= 10:
        arr[i] -= 10
for i in arr[1:]:
    print(i,end=' ')