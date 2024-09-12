n,m = map(int, input().split())
graph = [[0]*(m+1) for _ in range(n+1)]
dxs, dys = [0,1,0,-1], [1,0,-1,0]

def in_range(x,y):
    return x>=1 and x<n+1 and y>=1 and y<m+1

x,y = 1,1
graph[x][y] = 1
dir_num = 0

for i in range(2,n*m+1):
    nx,ny = x+dxs[dir_num], y+dys[dir_num]
    if not in_range(nx,ny) or graph[nx][ny] != 0:
        dir_num = (dir_num+1)%4
    x, y = x+dxs[dir_num], y+dys[dir_num]
    graph[x][y] = i

for raw in graph[1:]:
    for elem in raw[1:]:
        print(elem, end=' ')
    print()