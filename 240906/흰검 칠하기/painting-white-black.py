n = int(input())
comm = [list(map(str, input().split())) for _ in range(n)]
wb = [0]*(10**5)*2
cnt = [0]*(10**5)*2
t = 10**5

for x, d in comm:
    x = int(x)
    if d=='R':
        cx = x + t
        for i in range(t, cx):
            cnt[i]+=1
            wb[i] = 2#검은색 2
    else:
        cx = t-x
        for i in range(cx,t):
            cnt[i]+=1
            wb[i] = 1#흰색 1
    t=cx

w,b,g = 0,0,0
for i in range((10**5)*2):
    if cnt[i]<4 and wb[i]==1:
        w+=1
    elif cnt[i]<4 and wb[i]==2:
        b+=1
    elif cnt[i]>=4:
        g+=1

print(w,b,g,end=' ')