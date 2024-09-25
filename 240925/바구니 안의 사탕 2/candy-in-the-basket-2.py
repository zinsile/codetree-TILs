n,k = map(int, input().split())
arr = [0]*101
for _ in range(n):
    t,p = map(int, input().split())
    arr[p] += t

def in_range(i):
    return 0>=i and 101>=i

maxcan = 0
for i in range(k,100-k+1):
    subcan = sum(arr[i-k:i+k+1])
    # print(subcan)
    maxcan = max(maxcan, subcan)

print(maxcan)