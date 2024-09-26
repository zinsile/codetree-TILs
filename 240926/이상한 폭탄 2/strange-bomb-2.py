n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]

t = 0
for i in range(n):
    for j in range(i+1,n):
        if arr[i] == arr[j] and j-i<=k:
            t = max(t,arr[i])
if t == 0:
    print(-1)
else: print(t)