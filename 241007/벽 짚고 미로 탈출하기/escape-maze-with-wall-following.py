n = int(input())
start_x, start_y = map(int, input().split())
grid = [list(map(str, input())) for _ in range(n)]

x = start_x - 1
y = start_y - 1

for i in range(n):
    for j in range(n):
        if grid[i][j] == '#':
            grid[i][j] = 1
        else:
            grid[i][j] = 0


def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n


dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

d = 0
time = 0
escape = False
while True:
    if escape:
        break
    nx, ny = x + dx[d], y + dy[d]
    # 1. 새로 가려는 곳이 격자 밖이라면
    if not in_range(nx, ny):
        escape = True
        time += 1
        break

    # 2. 새로 가려는 곳이 벽이라면:
    if grid[nx][ny] == 1:
        for _ in range(2):
            # 2.1 반시계 회전한 뒤 전진
            d = (4 + d - 1) % 4
            nx, ny = x + dx[d], y + dy[d]
            if not in_range(nx, ny):
                escape = True
                time += 1
                break
            if grid[nx][ny] == 0:
                # 이동
                time += 1
                x, y = nx, ny
                break
    if escape:
        break
    nd = (d + 1) % 4
    # 3. 새로 가려는 곳이 비어있고 새로 가려는곳 아래가 벽이라면:
    if grid[nx][ny] == 0 and grid[nx + dx[nd]][ny] == 1:
        # 3.1 새로 가려는 곳으로 전진
        time += 1
        x, y = nx , ny

    # 4. 새로 가려는 곳이 비어있고 새로 가려는곳 아래가 길이라면:
    if grid[nx][ny] == 0 and grid[nx + dx[nd]][ny] == 0:
        # 4.1 한칸 앞으로(새로 가려는 곳) 시계방향 회전한 뒤 , 다시 한칸 앞으로
        x, y = nx+dx[nd], ny+dy[nd]
        time += 2
        d = nd

    if x == start_x - 1 and y == start_y - 1:
        break

if escape:
    print(time)
else:
    print(-1)