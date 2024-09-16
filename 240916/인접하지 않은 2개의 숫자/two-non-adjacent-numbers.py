n = int(input())
arr = list(map(int, input().split()))
maxans = 0

for i in range(n-2):
    for j in range(i+2,n):
        maxans = max(maxans, arr[i]+arr[j])

print(maxans)