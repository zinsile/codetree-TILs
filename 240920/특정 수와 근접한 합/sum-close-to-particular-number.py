n,s = map(int, input().split())
arr = list(map(int, input().split()))

curmin = 10**6

for i in range(n):
    for j in range(i,n):
        add = sum(arr)-arr[i]-arr[j]
        curmin = min(curmin, abs(s-add))

print(curmin)