n,r,c = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

def in_range(x,y):
    return x>=0 and x<n and y>=0 and y<n

x, y = r-1, c-1
dxs, dys = [-1,1,0,0], [0,0,-1,1]
#step0. 현재 위치 프린트
print(grid[x][y], end=' ')
while True:
    #step1. 상하좌우 탐색 : 현재보다 더 큰 거 있을때 바로 탐색 종료
    did_move = False
    for dx,dy in zip(dxs, dys):
        if in_range(x+dx, y+dy) and grid[x][y] < grid[x+dx][y+dy]:
            #step2. 이동
            x, y = x+dx, y+dy
            print(grid[x][y], end=' ')
            did_move = True
    #    1.1. 만약 없을 경우 종료
    if not did_move:
        break