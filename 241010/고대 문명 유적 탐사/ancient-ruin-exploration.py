K, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(5)]
wall = list(map(int, input().split()))

ans = []

def in_range(x,y):
    return 0<=x<5 and 0<=y<5

def value_count(arr,flag):
    v = [[False]*5 for _ in range(5)]
    result = 0
    for i in range(5):
        for j in range(5):
            q = []
            spot = set()
            q.append((i,j))
            spot.add((i,j))
            v[i][j] = True
            cnt = 1

            while q:
                x,y = q.pop(0)
                for dx,dy in [(-1,0),(0,1),(1,0),(0,-1)]:
                    nx, ny = x+dx, y+dy
                    # 범위내, 미방문, 조건: [x][y]와 같은 값
                    if in_range(nx,ny) and not v[nx][ny] and arr[x][y] == arr[nx][ny]:
                        q.append((nx,ny))
                        spot.add((nx,ny))
                        v[nx][ny] = True
                        cnt += 1
            if cnt >= 3:
                if flag == 1:
                    # 유물자리 초기화
                    for x, y in spot:
                        arr[x][y] = 0
                result += cnt
    return result, arr

def rotate(arr,x,y,rot):
    narr = [x[:] for x in arr]
    for _ in range(rot):
        for i in range(3):
            for j in range(3):
                narr[x+i][y+j] = arr[x+3-j-1][y+i]
    return narr


# K턴 진행
for _ in range(K):
    # [1] 탐사진행
    # 최종 회전 격자 구하기 : 각도->열->행
    max_cnt = 0
    for rot in range(1,4):
        for i in range(3):
            for j in range(3):
                narr = [x[:] for x in arr]
                narr = rotate(narr,i,j,rot) # rot 회수만큼 시계방향 90도 회전
                cnt, narr = value_count(narr,0)
                if max_cnt < cnt:
                    max_cnt = cnt
                    marr = narr

    if max_cnt == 0: #탐사진행시 어떤 회전도 유물을 못만들어내면 모든 탐사 종료
        break
    # [2] 유물획득
    arr = marr
    cnt = 0
    while True: # 유물 획득 안될때까지 획득
        t, arr = value_count(arr,1)

        if t == 0: #만약 탐사 안된다면 이번 턴 종료
            break
        cnt += t
        # 유물자리 채우기
        for y in range(5):
            for x in range(4,-1,-1):
                if arr[x][y] == 0:
                    arr[x][y] = wall.pop(0)
    ans.append(cnt)
print(*ans)