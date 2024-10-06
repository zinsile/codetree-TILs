OUT_OF_GRID = -1

# 변수 선언 및 입력:
n, m = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
next_grid = [
    [0 for _ in range(n)]
    for _ in range(n)
]


def get_bomb_row(bomb_col):
    for i in range(n):
        if grid[i][bomb_col] != 0:
            return i
    return OUT_OF_GRID

def bomb_in_range(x,y,center_x,center_y, number):
    return (x==center_x or y==center_y) and \
    abs(x-center_x)+abs(y-center_y) <= number - 1

def bomb(bomb_row, bomb_col):
    #step1. 십자모양 폭탄 터치기
    number = grid[bomb_row][bomb_col]
    for i in range(n):
        for j in range(n):
            if bomb_in_range(i,j,bomb_row,bomb_col,number):
                grid[i][j] = 0
    
    #step2. 떨어지는 모양 next_grid에 담기
    for i in range(n):
        for j in range(n):
            next_grid[i][j] = 0
    
    for i in range(n):
        temp_row = n-1
        for j in range(n-1,-1,-1):
            if not grid[j][i]:
                continue
            next_grid[temp_row][i] = grid[j][i]
            temp_row -= 1
    
    #step3. next_grid -> grid로 옮기기
    for i in range(n):
        for j in range(n):
            grid[i][j] = next_grid[i][j]


for _ in range(m):
    bomb_col = int(input()) - 1

    bomb_row = get_bomb_row(bomb_col)

    if bomb_row == OUT_OF_GRID:
        continue
    
    bomb(bomb_row, bomb_col)

for i in range(n):
    for j in range(n):
        print(grid[i][j], end=' ')
    print()