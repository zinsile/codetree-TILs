n,m = map(int, input().split())
graph = [[0]*m for _ in range(n)]
graph[0][0] = 1
dxs, dys = [1,0,-1,0], [0,1,0,-1]
def in_range(x,y):
    return x>=0 and x<n and y>=0 and y<m
dir_num = 0
x,y = 0,0

for i in range(2,n*m+1):
    nx, ny = x+dxs[dir_num], y+dys[dir_num]
    if not in_range(nx,ny) or graph[nx][ny]!=0:
        dir_num = (dir_num+1)%4
    
    x,y = x+dxs[dir_num], y+dys[dir_num]
    graph[x][y] = i

for raw in graph:
    for elem in raw:
        print(elem, end=' ')
    print()