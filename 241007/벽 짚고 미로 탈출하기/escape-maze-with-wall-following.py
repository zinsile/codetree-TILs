n = int(input())
start_x, start_y = map(int, input().split())
grid = [list(map(str, input())) for _ in range(n)]
visited = [[[False for _ in range(4)] for _ in range(n)] for _ in range(n)]

curr_x = start_x - 1
curr_y = start_y - 1

for i in range(n):
    for j in range(n):
        if grid[i][j] == '#':
            grid[i][j] = 1
        else:
            grid[i][j] = 0

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

d = 0
time = 0

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def simulate():
    global curr_x, curr_y, d, time
    if visited[curr_x][curr_y][d]:
        time = -1
        curr_x, curr_y = -1, -1
        return

    visited[curr_x][curr_y][d] = True
    nx, ny = curr_x + dx[d], curr_y + dy[d]
    nd = (d+1) % 4
    rx, ry = nx + dx[nd], ny + dy[nd]

    # 1. 범위 밖일경우
    if not in_range(nx, ny):
        time += 1
        curr_x, curr_y, = nx, ny
        return

    # 2. 벽일경우
    elif grid[nx][ny] == 1:\
        d = (4+d-1) % 4

    # 3. 이동가능할 경우
    else:
        # 3.1. 오른 쪽 벽일경우
        if grid[rx][ry] == 1:
            time += 1
            curr_x, curr_y = nx, ny
        # 3.2. 오른 쪽 벽 아닐경우
        else:
            time += 2
            curr_x, curr_y = rx, ry
            d = nd

while in_range(curr_x, curr_y):
    simulate()

print(time)