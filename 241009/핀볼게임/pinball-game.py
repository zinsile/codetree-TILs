n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

start_spots = []
start_spots += [(0,y,0) for y in range(n)]
start_spots += [(x,n-1,3) for x in range(n)]
start_spots += [(n-1,y,2) for y in range(n)]
start_spots += [(x,0,1) for x in range(n)]

dx, dy = [1,0,-1,0], [0,1,0,-1]

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def moving(x,y,d):
    time = 1
    if graph[x][y] == 1:
        d = abs(3-d)
    if graph[x][y] == 2:
         d= d ^ 1
    while True:
        nx, ny = x+dx[d], y+dy[d]
        # 격자 밖 벗어날 경우
        if not in_range(nx,ny):
            time += 1
            break
        # 빈시판 있을경우 nx,ny로 이동한 뒤 d바꿔놓기
        if graph[nx][ny] == 1:
            d = abs(3-d)
        if graph[nx][ny] == 2:
            d = d ^ 1
        x, y = nx, ny
        #시간 더하기
        time += 1
    return time

max_time = 0
for sx, sy, d in start_spots:
    time = moving(sx,sy,d)
    max_time = max(max_time, time)

print(max_time)