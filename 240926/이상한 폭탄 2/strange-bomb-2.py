n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]

t = 0
for i in range(n):
    for j in range(i+1,n):
        if arr[i] == arr[j] and j-i<=k:
            for k in range(i,j+1):
                t = max(t,arr[k])
print(t)