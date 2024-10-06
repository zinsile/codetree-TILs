NONE = -1
n = 4
grid = [list(map(int, input().split())) for _ in range(n)]
d = input()
temp_grid = [[0 for _ in range(n)] for _ in range(n)]


def shift_down():
    temp_grid_reset()

    for i in range(n):
        keep_num, temp_row = NONE, n - 1

        for j in range(n-1,-1,-1):

            if not grid[j][i]:
                continue

            if keep_num == NONE:
                keep_num = grid[j][i]
                temp_grid[temp_row][i] = grid[j][i]
                continue

            if keep_num == grid[j][i]:
                temp_grid[temp_row][i] = keep_num * 2
                temp_row -= 1
                keep_num = NONE
                continue

            if keep_num != grid[j][i]:
                temp_grid[temp_row][i] = keep_num
                temp_row -= 1
                keep_num = grid[j][i]
                temp_grid[temp_row][i] = keep_num

    for i in range(n):
        for j in range(n):
            grid[i][j] = temp_grid[i][j]


def temp_grid_reset():
    for i in range(n):
        for j in range(n):
            temp_grid[i][j] = 0


def rotate():
    temp_grid_reset()

    for i in range(n):
        for j in range(n):
            temp_grid[i][j] = grid[n - j - 1][i]

    for i in range(n):
        for j in range(n):
            grid[i][j] = temp_grid[i][j]


def simulate():
    direction = {'D': 0, 'R': 1, 'U': 2, 'L': 3}
    for _ in range(direction[d]):
        rotate()
    shift_down()
    for _ in range(4 - direction[d]):
        rotate()


simulate()

for row in grid:
    for elem in row:
        print(elem, end=' ')
    print()