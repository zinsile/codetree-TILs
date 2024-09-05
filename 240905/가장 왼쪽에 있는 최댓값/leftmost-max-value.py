n = int(input())
arr = list(map(int, input().split()))

while True:
    maxs = -1
    if n+1 == 1:
        break
    for i in range(n):
        if arr[i] > maxs:
            n = i
            maxs = arr[i]
    print(n+1,end=' ')