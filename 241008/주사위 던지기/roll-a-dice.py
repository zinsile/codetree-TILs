n, m, r, c = map(int, input().split())
commd = list(map(str, input().split()))

grid = [[0 for _ in range(n)] for _ in range(n)]
dirc = {'U':0, 'D':1, 'L':2, 'R':3}
dx, dy = [-1,1,0,0],[0,0,-1,1]
x, y = r-1, c-1
U, F, R = 1, 2, 3
grid[x][y] = 7-U

def in_range(x,y):
    return x>=0 and x<n and y>=0 and y<n

for d in commd:
    nx, ny = x+dx[dirc[d]], y+dy[dirc[d]]

    if not in_range(nx, ny):
        continue
    
    if dirc[d] == 0:
        U, F, R = F, 7-U, R
    elif dirc[d] == 1:
        U, F, R = 7-F, U, R
    elif dirc[d] == 2:
        U, F, R = R, F, 7-U
    else:
        U, F, R = 7-R, F, U

    grid[nx][ny] = 7-U
    x, y = nx, ny

ans = 0
for i in range(n):
    for j in range(n):
        ans += grid[i][j]

print(ans)