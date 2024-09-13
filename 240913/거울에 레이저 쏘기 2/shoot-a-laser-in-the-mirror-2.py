n = int(input())
graph =[list(input()) for _ in range(n)]
num = int(input())

#'\':dir_num = (dir_num-1+4)%4, '/':dir_num = (dir_num+1)%4

# 주어진 숫자에 따라
# 시작 위치와 방향을 구합니다.
def initialize(num):
    if num <= n:
        return 0, num-1, 0
    elif num <= 2*n:
        return num-n-1, n-1, 1
    elif num <= 3*n:
        return n-1, n-(num-2*n), 2
    else:
        return n-(num-3*n), 0, 3


def in_range(x,y):
    return 0 <= x and x<n and 0<=y and y<n

def move(x,y,next_dir):
    dxs,dys = [1,0,-1,0], [0,-1,0,1]
    nx,ny = x+dxs[next_dir], y+dys[next_dir]
    return nx, ny, next_dir

def simulate(x,y,dir_num):
    move_num = 0
    while in_range(x,y):
        if graph[x][y] == '/':
            x,y,dir_num = move(x, y, dir_num ^ 1)
        else:
            x,y,dir_num = move(x, y, 3 - dir_num)
        move_num += 1
    return move_num

x,y,dir_num = initialize(num)
move_num = simulate(x,y,dir_num)
print(move_num)