n,m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

def shift_down():
    temp_grid = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        temp_row = n-1
        for j in range(n-1,-1,-1):
            if grid[j][i] == 0:
                continue
            temp_grid[temp_row][i] = grid[j][i]
            temp_row -= 1
    
    for i in range(n):
        for j in range(n):
            grid[i][j] = temp_grid[i][j]

def bomb(x,y):
    for i in range(n):
        for j in range(n):
            if x==i and y==j:
                continue
            if (x==i or y==j) and (abs(x-i)+abs(y-j) <= grid[x][y]-1):
                grid[i][j] = 0
    grid[x][y] = 0

def choise_bomb(col):
    for i in range(n):
        if grid[i][col] > 0:
            return i
    return -1

def simulate(col):
    x = choise_bomb(col)
    if x == -1:
        return
    bomb(x,col)
    shift_down()

for _ in range(m):
    c = int(input())
    simulate(c-1)

for row in grid:
    for elem in row:
        print(elem, end=' ')
    print()