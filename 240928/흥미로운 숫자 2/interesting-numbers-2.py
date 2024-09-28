x,y = map(int, input().split())

cnt = 0
for i in range(x,y+1):
    arr = list(map(int, list(str(i))))
    t = []
    for a in arr:
        if a not in t:
            t.append(a)
    if len(t) == 2:
        cnt += 1

print(cnt)