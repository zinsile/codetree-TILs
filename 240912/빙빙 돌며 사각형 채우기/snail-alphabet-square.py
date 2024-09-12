n,m = map(int,input().split())
graph = [[0]*m for _ in range(n)]
dxs,dys = [0,1,0,-1], [1,0,-1,0]
x,y,dir_num = 0,0,0
graph[0][0] = 'A'

def in_range(x,y):
    return x>=0 and x<n and y>=0 and y<m

c = 66
for i in range(n*m-1):
    
    nx,ny = x+dxs[dir_num], y+dys[dir_num]
    if not in_range(nx,ny) or graph[nx][ny]!=0:
        dir_num = (dir_num+1)%4
    
    x,y = x+dxs[dir_num], y+dys[dir_num]
    
    if c == 91:
        c=65
    graph[x][y] = chr(c)
    c+=1

for raw in graph:
    for elem in raw:
        print(elem, end=' ')
    print()