n, m, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
next_grid = [[0 for _ in range(n)] for _ in range(n)]


def next_grid_reset():
    for i in range(n):
        for j in range(n):
            next_grid[i][j] = 0


def shift_down():
    next_grid_reset()
    for i in range(n):
        temp_row = n - 1
        for j in range(n - 1, -1, -1):
            if not grid[j][i]:
                continue
            next_grid[temp_row][i] = grid[j][i]
            temp_row -= 1

    for i in range(n):
        for j in range(n):
            grid[i][j] = next_grid[i][j]


def rotate():
    next_grid_reset()
    for i in range(n):
        for j in range(n):
            next_grid[i][j] = grid[n - j - 1][i]

    for i in range(n):
        for j in range(n):
            grid[i][j] = next_grid[i][j]


def bomb():
    for i in range(n):
        cnt, start_index, keep_num = 1, 0, -1
        for j in range(n):
            if not grid[j][i]:
                continue
            if keep_num == -1:
                keep_num = grid[j][i]
                start_index = j
                continue
            if keep_num == grid[j][i]:
                cnt += 1
                if cnt >= m and j==n-1:
                    for idx in range(start_index, n):
                        grid[idx][i] = 0
                continue
            if keep_num != grid[j][i] and cnt < m:
                start_index = j
                cnt = 1
                keep_num = grid[j][i]
                continue
            if keep_num != grid[j][i] and cnt >= m:
                for idx in range(start_index, j):
                    grid[idx][i] = 0
                cnt = 1
                start_index = j
                keep_num = grid[j][i]

def simulate():
    bomb()
    shift_down()
    rotate()
    shift_down()


for _ in range(k):
    simulate()

bomb()

ans = 0
for i in range(n):
    for j in range(n):
        if grid[i][j] != 0:
            ans += 1

if n==1:
    print(0)
else:
    print(ans)