head_x, head_y = 0, 0
tail_x, tail_y = -1, -1


n, m, k = map(int, input().split())
apples = [list(map(int, input().split())) for _ in range(m)]
infos = [list(map(str, input().split())) for _ in range(k)]
graph = [[0]*n for _ in range(n)]

for x, y in apples:
    graph[x-1][y-1] = 2
graph[head_x][head_y] = 1
snake = []
snake.append((head_x,head_y))
# graph에서 2는 사과 / 1은 뱀

dx, dy = [-1,1,0,0],[0,0,1,-1]
dirc = {'U':0, 'D':1, 'R':2, 'L':3}


def in_range(x,y):
    return 0<=x<n and 0<=y<n

def moving(new_head_x, new_head_y,d):
    global head_x, head_y, tail_x, tail_y
    # 움직이려는 곳에 사과가 있는 경우
    if graph[new_head_x][new_head_y] == 2:
        snake.insert(0,(new_head_x,new_head_y))
        head_x, head_y = new_head_x, new_head_y
        graph[head_x][head_y] = 1
    # 빈공간인 경우
    else:
        tail_x, tail_y = snake.pop()
        head_x,head_y = new_head_x, new_head_y
        # tail_x, tail_y = snake.pop()
        snake.insert(0,(new_head_x, new_head_y))
        graph[tail_x][tail_y] = 0
        graph[head_x][head_y] = 1

# def print_graph():
#     for row in graph:
#         for elem in row:
#             print(elem, end=' ')
#         print()
#     print("-----")

time = 0
game_end = False
for direc, p in infos:
    d = dirc[direc]
    for _ in range(int(p)):
        time += 1
        new_head_x, new_head_y = head_x + dx[d], head_y + dy[d]
        #격자 벗어나면 게임종료
        if not in_range(new_head_x,new_head_y):
            game_end = True
            break
        #몸이 꼬여 서로 겹칠경우 종료
        if graph[new_head_x][new_head_y] == 1 and (new_head_x != tail_x and new_head_y != tail_y):
            game_end = True
            break
        # 사과가 있거나 빈공간이면 뱀 이동
        moving(new_head_x,new_head_y,d)
        # print_graph()
    if game_end:#격자 벗어나면 게임종료
        break

print(time)