arr = list(map(int, input().split()))
index = len(arr)
for i,elem in enumerate(arr):
    if elem == 0:
        index = i-1
        break
for i in arr[index::-1]:
    print(i,end=' ')