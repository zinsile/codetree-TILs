def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def simulate():
    # 구슬 찾기
    temp = [[0] * n for _ in range(n)]
    d_temp = [[0] * n for _ in range(n)]
    id_temp = [[0] * n for _ in range(n)]
    moving = False
    # print_graph(g_exist)
    for i in range(n):
        for j in range(n):
            if g_exist[i][j] == 0:
                continue
            # print_graph(g_exist)
            moving = True
            d = g_dirc[i][j]
            idx = g_id[i][j]
            nx, ny = i + dx[d], j + dy[d]
            # 벽에 부딪히면 x,y는 움직이지 않고 방향만 바꿈
            if not in_range(nx, ny):
                if d==1:
                    d=3
                elif d==3:
                    d=1
                elif d==2:
                    d=4
                else:
                    d=2
                nx,ny = i,j
            # 이동 가능 하다면 방향 그대로 위치만 바뀜
            # print(nx, ny, d)
            temp[nx][ny] += 1
            d_temp[nx][ny] = d
            id_temp[nx][ny] = idx
    #구슬이 다 없어져서 움직일 구슬 없을때
    if not moving:
        return False
    # print_graph(temp)
    # 충돌하면 exist에서 삭제하고 dirc도 삭제하기
    for i in range(n):
        for j in range(n):
            if temp[i][j] > 1:
                temp[i][j] = 0
                d_temp[i][j] = 0
                id_temp[i][j] = 0
    # print_graph(temp)
    # 결과 옮기기
    # print_graph(temp)
    for i in range(n):
        for j in range(n):
            g_exist[i][j] = temp[i][j]
            g_dirc[i][j] = d_temp[i][j]
            g_id[i][j] = id_temp[i][j]

    # #방문 기록 체크
    # for i in range(n):
    #     for j in range(n):
    #         # 방문한 곳이면 게임 종료
    #         d = g_dirc[i][j]
    #         id = g_id[i][j]
    #         if g_exist[i][j] == 1 and id in visit[i][j][d]:
    #             return False
    #         # 방문 안했던 곳이면 방문기록 남기기
    #         if not g_dirc[i][j] in visit[i][j][g_id[i][j]] and g_exist[i][j] == 1:
    #             visit[i][j][g_id[i][j]]+=g_dirc[i][j]
    # print_graph(g_exist)
    return True


def print_graph(name):
    for row in name:
        for elem in row:
            print(elem, end=' ')
        print()
    print("-----")


dirc = {'U': 1, 'R': 2, 'D': 3, 'L': 4}
dx, dy = [0,-1, 0, 1, 0], [0,0, 1, 0, -1]

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    # visit = [[[0 for _ in range(5)]for _ in range(n)] for _ in range(n)]  # 구슬 방문기록
    g_exist = [[0] * n for _ in range(n)]  # 구슬 존재 그래프 0:없음, 1:있음
    g_dirc = [[0] * n for _ in range(n)]  # 구슬 방향 정보 그래프 :  구슬 존재할때 움직일 방향 알기 위함
    temp = [[0] * n for _ in range(n)]  # 두개이상 충돌할때 알기 위한 그래프
    g_id = [[0] * n for _ in range(n)]
    for id in range(1,m+1):
        x, y, direction = map(str, input().split())
        x, y = int(x), int(y)
        d = dirc[direction]
        g_exist[x - 1][y - 1] = 1
        g_dirc[x - 1][y - 1] = d
        g_id[x - 1][y - 1] = id
        # visit[x - 1][y - 1][d].insert(-1,id)
    keepgoing = True
    for _ in range(2*n):
        # id 구슬이 같은 방향으로 같은자리에 방문하면 무한루프이므로 케이스 종료
        if not keepgoing:  # not visit[x][y][id][d]
            break
        # 구슬 찾아서 / 방향대로 옮기고 방향 바꾸고/ 충돌확인해서 / 총결과 g_exist에 저장 / 같은 자리 방문했는지 확인 not visit[x][y][id][d]
        keepgoing = simulate()

    ans = 0
    for i in range(n):
        for j in range(n):
            if g_exist[i][j] == 1:
                ans+=1
    print(ans)