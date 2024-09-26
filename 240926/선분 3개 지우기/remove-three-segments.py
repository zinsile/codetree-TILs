n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

def overlap_check(i,j,k):
    line = [0]*101
    for t in range(n):
        if t == i or t == j or t == k:
            continue
        a,b = arr[t]
        for c in range(a,b+1):
            line[c] += 1
    for l in line:
        if l>1:
            return False
    return True

cnt = 0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if overlap_check(i,j,k):
                cnt += 1
print(cnt)