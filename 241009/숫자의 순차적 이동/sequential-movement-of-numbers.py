def find_num(num):
    for i in range(n):
        for j in range(n):
            if graph[i][j] == num:
                return (i,j)

def in_range(x, y):
    return 0<=x<n and 0<=y<n

def biggist(x,y):
    dxs, dys = [-1,1,0,0,-1,-1,1,1],[0,0,1,-1,-1,1,1,-1]
    rx, ry = 0, 0
    max_n = 0
    for dx, dy in zip(dxs,dys):
        nx, ny = x+dx, y+dy
        if in_range(nx, ny) and graph[nx][ny]>max_n:
            max_n = graph[nx][ny]
            rx, ry = nx, ny
    return rx, ry

def simulate():
    for num in range(1, n**2+1):
        # 숫자 num 위치 찾아서 반환
        num_x, num_y = find_num(num)
        # 8방향 중 가장 큰 숫자 위치 찾아서 반환 후 num위치랑 교환
        temp = 0
        bs_x, bs_y = biggist(num_x, num_y)
        temp = graph[bs_x][bs_y]
        graph[bs_x][bs_y] = num
        graph[num_x][num_y] = temp

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

for _ in range(m):
    simulate()

for row in graph:
    for elem in row:
        print(elem, end=' ')
    print()