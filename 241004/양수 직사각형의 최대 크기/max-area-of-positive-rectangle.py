n,m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

def in_range(x,y):
    return x>=0 and x<n and y>=0 and y<m 

def checking_subarea(x,y,w,h):
    if not in_range(x+w,y+h):
        return 0
    for i in range(x,x+w+1):
        for j in range(y,y+h+1):
            if graph[i][j]<0:
                return 0
    return (w+1)*(h+1)

ans = 0
for i in range(n):
    for j in range(m):
        for w in range(n):
            for h in range(m):
                ans = max(ans, checking_subarea(i,j,w,h))

if ans==0:
    print(-1)
else: print(ans)