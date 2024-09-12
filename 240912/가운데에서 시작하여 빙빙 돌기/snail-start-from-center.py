n = int(input())
graph = [[0]*n for _ in range(n)]
dxs, dys = [0,-1,0,1], [-1,0,1,0]
x, y, dir_num = n-1, n-1, 0
graph[x][y] = n*n
def in_range(x,y):
    return x>=0 and x<n and y>=0 and y<n

for i in range(n*n-1,0,-1):
    
    nx,ny = x+dxs[dir_num], y+dys[dir_num]
    if not in_range(nx,ny) or graph[nx][ny]!=0:
        dir_num = (dir_num+1)%4
    
    x,y = x+dxs[dir_num], y+dys[dir_num]
    graph[x][y] = i

for raw in graph:
    for elem in raw:
        print(elem, end=' ')
    print()