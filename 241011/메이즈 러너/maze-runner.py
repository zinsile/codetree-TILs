N,M,K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
units = {}
for idx in range(1, M+1):
    x, y = list(map(int, input().split()))
    units[idx] = [x-1,y-1]
ex, ey = map(int, input().split())
ex, ey = ex-1, ey-1

def move_units():
    cnt = 0
    remove = set()
    for idx in units:
        x,y = units[idx]
        min_dis = abs(ex-x)+abs(ey-y)
        min_x, min_y = x, y

        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x+dx, y+dy
            if 0>nx or nx>=N or 0>ny or ny>=N:
                continue
            ndis = abs(ex-nx)+abs(ey-ny)
            if ndis < min_dis and arr[nx][ny]==0:
                min_dis = ndis
                min_x, min_y = nx, ny
        if min_x != x or min_y != y:
            cnt += 1
            if min_x==ex and min_y==ey:
                remove.add(idx)
            else:
                units[idx] = [min_x, min_y]
    return cnt, remove

def square():
    for t in range(2,N+1):
        for i in range(N-(t-1)):
            for j in range(N-(t-1)):
                if not (i<=ex<i+t and j<=ey<j+t):
                    continue
                for idx in units:
                    x, y = units[idx]
                    if i<=x<i+t and j<=y<j+t:
                        return i, j, t

def rotate(arr, ex, ey):
    narr = [x[:] for x in arr]
    sx,sy,square_size = square()
    # 우선 정사각형 안에 있는 벽들을 1 감소시킵니다.
    for x in range(sx, sx + square_size):
        for y in range(sy, sy + square_size):
            if arr[x][y]:
                arr[x][y] -= 1
    # 정사각형을 시계방향으로 90' 회전합니다.
    for x in range(sx, sx + square_size):
        for y in range(sy, sy + square_size):
            # Step 1. (sx, sy)를 (0, 0)으로 옮겨주는 변환을 진행합니다.
            ox, oy = x - sx, y - sy
            # Step 2. 변환된 상태에서는 회전 이후의 좌표가 (x, y) . (y, square_n - x - 1)가 됩니다.
            rx, ry = oy, square_size - ox - 1
            # Step 3. 다시 (sx, sy)를 더해줍니다.
            narr[rx + sx][ry + sy] = arr[x][y]
    # next_board 값을 현재 board에 옮겨줍니다.
    for x in range(sx, sx + square_size):
        for y in range(sy, sy + square_size):
            arr[x][y] = narr[x][y]
    ##############################################
    # m명의 참가자들을 모두 확인합니다.
    for i in units:
        tx, ty = units[i]
        # 해당 참가자가 정사각형 안에 포함되어 있을 때에만 회전시킵니다.
        if sx <= tx and tx < sx + square_size and sy <= ty and ty < sy + square_size:
            # Step 1. (sx, sy)를 (0, 0)으로 옮겨주는 변환을 진행합니다.
            ox, oy = tx - sx, ty - sy
            # Step 2. 변환된 상태에서는 회전 이후의 좌표가 (x, y) . (y, square_n - x - 1)가 됩니다.
            rx, ry = oy, square_size - ox - 1
            # Step 3. 다시 (sx, sy)를 더해줍니다.
            units[i] = [rx + sx, ry + sy]

    # 출구에도 회전을 진행합니다.
    if sx <= ex and ex < sx + square_size and sy <= ey and ey < sy + square_size:
        # Step 1. (sx, sy)를 (0, 0)으로 옮겨주는 변환을 진행합니다.
        ox, oy = ex - sx, ey - sy
        # Step 2. 변환된 상태에서는 회전 이후의 좌표가 (x, y) . (y, square_n - x - 1)가 됩니다.
        rx, ry = oy, square_size - ox - 1
        # Step 3. 다시 (sx, sy)를 더해줍니다.
        nex,ney = (rx + sx, ry + sy)
    return narr,nex,ney

ans = 0
for _ in range(K):
    cnt, remove = move_units()
    ans += cnt
    if remove:
        for idx in remove:
            units.pop(idx)
    if not units:
        break
    arr, ex, ey = rotate(arr, ex, ey)

print(ans)
print(ex+1, ey+1, end=' ')