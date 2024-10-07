n, m, k = map(int, input().split())
k = k-1
grid = [list(map(int, input().split())) for _ in range(n)]

def check_grid(row):
    for col in range(k, k+m):
        if grid[row][col] == 1:
            return False
    return True

while True:
    block_row = 0
    under_block = False
    #step1. 블록 떨어뜨리기 : 블럭 닿으면 under_block = True
    for row in range(1,n):
        if not check_grid(row): #하나라도 안비어있다면 
            block_row = row - 1
            under_block = True
            break
    #   1.1. 블록 1로 색칠
    for col in range(k, k+m):
        grid[block_row][col] = 1
    #step2. 놓인 위치 행이 0이거나 if under_block이면 : break
    if under_block or row == n-1 :
        break


for row in grid:
    for elem in row:
        print(elem, end=' ')
    print()