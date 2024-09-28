x,y = map(int, input().split())

cnt = 0
for i in range(x,y+1):
    arr = list(str(i))
    tmp1 = [int(a) for a in arr]
    tmp2 = [int(a) for a in arr[::-1]]
    if tmp1==tmp2:
        cnt += 1

print(cnt)