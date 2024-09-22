n,k = map(int, input().split())
arr = list(map(int,input().split()))

maxsum = 0
for i in range(n-k+1):
    maxsum = max(maxsum,sum(arr[i:i+k]))
print(maxsum)