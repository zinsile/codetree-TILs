import sys
n = int(input())
arr = list(map(int, input().split()))

min_diff = sys.maxsize
for i in range(n):
    arr[i] *= 2
    for j in range(n):
        remaining = []
        for k in range(n):
            if i!=k:
                remaining.append(arr[k])
        sub_diff = 0
        for l in range(1,n-1):
            sub_diff += abs(arr[l-1]-arr[l])
        min_diff = min(min_diff,sub_diff)

    arr[i] //= 2
print(min_diff)