n,k = map(int, input().split())
arr = [0]*10001

for _ in range(n):
    p,t = map(str,input().split())
    if t == 'G':
        arr[int(p)] += 1
    else:
        arr[int(p)] += 2

maxsco = 0
for i in range(1,10001-k+2):
    maxsco = max(maxsco, sum(arr[i:i+k+1]))

print(maxsco)