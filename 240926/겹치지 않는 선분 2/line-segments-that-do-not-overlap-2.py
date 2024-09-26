n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

#x1작은데 x2더 크거나
#x1더큰데 x2더 작거나

result = 0
for i in range(n):
    x1,x2 = arr[i]
    cnt = 0
    for j in range(n):
        if i==j:
            continue
        a1,a2 = arr[j]
        if x1<a1 and x2>a2:
            continue
        if x1>a1 and x2<a2:
            continue
        cnt += 1
    if cnt == n-1:
        result += 1

print(result)