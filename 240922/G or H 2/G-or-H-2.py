arr = [0]*101
n = int(input())
R = 0
for _ in range(n):
    p,alpha = input().split()
    R = max(R,int(p))
    if alpha=='G':
        arr[int(p)] = 1
    else: arr[int(p)] = 2

maxg, maxh, maxgh = 0,0,0
for i in range(R+1):
    for j in range(i,R+1):
        temp = False
        for k in range(i,j+1):
            if arr[k]==2:
                temp = True
        if not temp:
            maxg = max(maxg,j-i)

for i in range(R+1):
    for j in range(i,R+1):
        temp = False
        for k in range(i,j+1):
            if arr[k]==1:
                temp = True
        if not temp:
            maxh = max(maxh,j-i)

for i in range(R+1):
    for j in range(i,R+1):
        g,h = 0,0
        for k in range(i,j+1):
            if arr[k]==1:
                g+=1
            else: h+=1
        if g==h:
            maxgh = max(maxgh,j-i)

print(max(maxg,maxh,maxgh))