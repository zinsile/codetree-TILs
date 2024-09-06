n = int(input())
comm = [list(map(str, input().split())) for _ in range(n)]
line = [0]*(10**5)*2
t = 10**5

for x,d in comm:
    x = int(x)
    if d == 'R':
        for i in range(t,t+x):
            line[i] = 1
        t= t+x-1
    else:
        for i in range(t,t-x,-1):
            line[i] = -1
        t= t-x+1

w,b = 0,0
for i in line:
    if i == 1:
        b += 1
    elif i == -1:
        w += 1

print(w,b,end=' ')