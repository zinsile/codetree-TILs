n,m,r,c = map(int, input().split())
graph = [[0]*n for _ in range(n)]

x, y = r-1, c-1
graph[x][y] = 1
dxs, dys = [-1,0,1,0], [0,1,0,-1]

def in_range(x,y):
    return 0<=x<n and 0<=y<n

for t in range(1,m+1):
    k = 2**(t-1)
    temp = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not graph[i][j]:
                continue
            temp[i][j] = 1
            for dx, dy in zip(dxs, dys):
                nx, ny = i+k*dx, j+k*dy
                if not in_range(nx, ny):
                    continue
                temp[nx][ny] = 1
    for i in range(n):
        for j in range(n):
            graph[i][j] = temp[i][j]

ans = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            ans += 1

print(ans)