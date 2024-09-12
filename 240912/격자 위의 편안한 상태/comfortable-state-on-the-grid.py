n,m = tuple(map(int, input().split()))

graph = [[0]*(n+1) for _ in range(n+1)]
dxs, dys = [-1,0,1,0],[0,1,0,-1]
def in_range(x,y):
    return x>=1 and x<n+1 and y>=1 and y<n+1


for _ in range(m):
    r,c = map(int, input().split())
    graph[r][c] = 1
    cnt = 0
    for dx,dy in zip(dxs,dys):
        nr,nc = r+dx, c+dy
        if in_range(nr,nc) and graph[nr][nc]==1:
            cnt+=1
    if cnt==3:
        print(1)
    else:print(0)