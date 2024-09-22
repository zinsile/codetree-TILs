n,k = map(int, input().split())
arr = [0]*101
for _ in range(n):
    t,p = map(int, input().split())
    arr[p] += t

maxcan = 0
for i in range(k+1,101-k+1):
    maxcan = max(maxcan,sum(arr[i-k:i+k+1]))
print(maxcan)