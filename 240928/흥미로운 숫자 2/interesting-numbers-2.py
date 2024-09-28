x,y = map(int, input().split())

cnt = 0
for i in range(x,y+1):
    arr = list(map(int, list(str(i))))
    tmp = [0]*10
    tmp2 = []
    for a in arr:
        if a not in tmp2:
            tmp2.append(a)
        tmp[a] += 1
    r = False
    if len(tmp2) == 2:
        for t in tmp2:
            if tmp[t] == 1 or tmp[t] == len(arr)-1:
                r = True
    if r:
        print(i)
        cnt+=1

print(cnt)