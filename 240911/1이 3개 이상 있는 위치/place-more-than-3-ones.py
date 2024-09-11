n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

dxs, dys = [0,1,0,-1], [1,0,-1,0]

def in_range(x,y):
    return x>=0 and x<n and y>=0 and y<n

res = 0

for i in range(n):
    for j in range(n):
        cnt = 0
        for dx,dy in zip(dxs, dys):
            nx,ny = i+dx, j+dy
            if in_range(nx,ny) and graph[nx][ny]==1:
                cnt+=1
        if cnt >= 3:
            res += 1

print(res)