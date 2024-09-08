n = int(input())
comm = [list(map(str, input().split())) for _ in range(n)]
wb = [0]*(10**5)*2
wcnt = [0]*(10**5)*2
bcnt = [0]*(10**5)*2
t = 10**5

for x, d in comm:
    x = int(x)
    if d=='R':
        for i in range(x):
            bcnt[t+i]+=1
            wb[t+i] = 2   #검은색2
        t =t+x-1
    else:
        for i in range(x):
            wcnt[t-i]+=1
            wb[t-i] = 1   #흰색1
        t = t-x+1

w,b,g = 0,0,0
for i in range((10**5)*2):
    if wcnt[i]>=2 and bcnt[i]>=2:
        g+=1
        continue
    elif wb[i]==1:
        w+=1
    elif wb[i]==2:
        b+=1


print(w,b,g,end=' ')