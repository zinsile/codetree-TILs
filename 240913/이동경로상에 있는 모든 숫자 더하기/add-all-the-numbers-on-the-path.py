n,t = map(int, input().split())
comm = list(input())
graph = [list(map(int, input().split())) for _ in range(n)]

x, y = n//2, n//2
res = graph[x][y]
dxs, dys = [-1,0,1,0], [0,1,0,-1]
dir_num = 0
def in_range(x,y):
    return x>=0 and x<n and y>=0 and y<n

for c in comm:

    if c=='L':
        dir_num = (dir_num-1+4)%4
    elif c=='R':
        dir_num = (dir_num+1)%4
    else:
        nx, ny = x+dxs[dir_num], y+dys[dir_num]
        if in_range(nx,ny):
            res += graph[nx][ny]
            x,y = nx,ny

print(res)