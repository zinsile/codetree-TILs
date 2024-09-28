n = int(input())
arr = list(map(int, input().split()))

cnt = [0]*101
for i in range(n):
    for j in range(i+1,n):
        if arr[i]>arr[j]:
            for k in range(arr[i]-1,arr[j],-1):
                if (arr[i]-k) == (k-arr[j]):
                    cnt[k] += 1
        else:
            for k in range(arr[i]+1,arr[j]):
                if (k-arr[i]) == (arr[j]-k):
                    cnt[k] += 1
print(max(cnt))