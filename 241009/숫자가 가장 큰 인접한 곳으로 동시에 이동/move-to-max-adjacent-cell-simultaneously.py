n,m,t = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
gexist= [[0]*n for _ in range(n)]
nextgexist = [[0]*n for _ in range(n)]

for _ in range(m):
    r,c = map(int, input().split())
    gexist[r-1][c-1] = 1


def in_range(x,y):
    return 0<=x<n and 0<=y<n

def get_next_spot(x,y):
    dx,dy = [-1,1,0,0], [0,0,-1,1]
    max_num = 0
    ans_x, ans_y= 0, 0
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if in_range(nx, ny) and graph[nx][ny] > max_num:
            max_num = graph[nx][ny]
            ans_x, ans_y = nx, ny
    return ans_x, ans_y

def simulate():
    nextgexist = [[0]*n for _ in range(n)] # 초기화
    
    for x in range(n):
        for y in range(n):
            if gexist[x][y] == 0:
                continue
            # 구슬표에 구슬이 존재하면 상하좌우 탐색해서 옮길 자리 반환
            nx, ny = get_next_spot(x,y)
            # next에 담아두기
            nextgexist[nx][ny] += 1
    
    # 원본으로 구슬 옮긴 후 결과 옮기기. 이때 동시에 충돌한 애들 삭제
    for i in range(n):
        for j in range(n):
            gexist[i][j] = nextgexist[i][j]
            if nextgexist[i][j] >= 2:
                gexist[i][j] = 0

def graph_print():
    for row in gexist:
        for elem in row:
            print(elem, end=' ')
        print()
    print("-----")

for _ in range(t):
    # graph_print()
    simulate()
    # graph_print()


ans = 0
for i in range(n):
    for j in range(n):
        ans += gexist[i][j]

print(ans)