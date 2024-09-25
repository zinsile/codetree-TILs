n,k = map(int, input().split())
arr = [0]*101
for _ in range(n):
    t,p = map(int, input().split())
    arr[p] += t

def in_range(i):
    return 0<=i and 100>=i

maxcan = 0
for i in range(101):
    subcan = arr[i]
    for j in range(k):
        j += 1
        if in_range(i-j):
            subcan += arr[i-j]
        if in_range(i+j):
            subcan += arr[i+j]
    maxcan = max(maxcan, subcan)

print(maxcan)