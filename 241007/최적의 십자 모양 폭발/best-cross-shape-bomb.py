n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
next_grid = [[0 for _ in range(n)] for _ in range(n)]
temp_grid = [[0 for _ in range(n)] for _ in range(n)]


def couple_cnt():
    cnt = 0
    for i in range(n):
        for j in range(n - 1):
            # if next_grid[i][j] == 0 or next_grid[j][i]==0:
            #     continue
            if next_grid[i][j] == next_grid[i][j + 1] and next_grid[i][j] != 0:
                cnt += 1
            if next_grid[j][i] == next_grid[j + 1][i] and next_grid[j][i] != 0:
                cnt += 1
    return cnt


def shift_down():
    for i in range(n):
        for j in range(n):
            temp_grid[i][j] = 0

    for i in range(n):
        temp_row = n - 1
        for j in range(n - 1, -1, -1):
            if next_grid[j][i] == 0:
                continue
            temp_grid[temp_row][i] = next_grid[j][i]
            temp_row -= 1

    for i in range(n):
        for j in range(n):
            next_grid[i][j] = temp_grid[i][j]


def explode(x, y):
    for i in range(n):
        for j in range(n):
            next_grid[i][j] = grid[i][j]

    num = grid[x][y]
    for i in range(n):
        for j in range(n):
            if (x == i or y == j) and (abs(x - i) + abs(y - j) <= num - 1):
                next_grid[i][j] = 0

max_couple_cnt = 0
for i in range(n):
    for j in range(n):
        explode(i, j)
        shift_down()
        cnt = couple_cnt()
        max_couple_cnt = max(max_couple_cnt, cnt)

print(max_couple_cnt)