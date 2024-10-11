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
            if not (0<=nx<N and 0<=ny<N):
                continue
            ndis = abs(ex-nx)+abs(ey-ny)
            if ndis < min_dis and arr[nx][ny] == 0:
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
        for i in range(N-1):
            for j in range(N-1):
                include = False
                for idx in units:
                    x, y = units[idx]
                    if i<=x<i+t and i<=ex<i+t and j<=y<j+t and j<=ey<j+t:
                        return i, j, t

def rotate(arr, ex, ey):
    narr = [x[:] for x in arr]
    npos = [[0]*N for _ in range(N)]
    nnpos = [[0]*N for _ in range(N)]
    npos[ex][ey] = -1 # 탈출구는 -1
    for idx in units:
        x,y = units[idx]
        npos[x][y] = idx # 사람은 번호로 1~M
    rx,ry,rt = square()

    for i in range(rt):
        for j in range(rt):
            narr[rx+i][ry+j] = arr[rx+rt-j-1][ry+i]
            if narr[rx+i][ry+j] > 0:
                narr[rx + i][ry + j] -= 1
            nnpos[rx+i][ry+j] = npos[rx+rt-j-1][ry+i]
            if nnpos[rx+i][ry+j] == -1:
                ex,ey = rx+i, ry+j
            if nnpos[rx+i][ry+j] > 0:
                units[nnpos[rx+i][ry+j]] = [rx+i, ry+j]
    return narr,ex,ey

ans = 0
for _ in range(K):
    if not units:
        break
    cnt, remove = move_units()
    ans += cnt
    if remove:
        for idx in remove:
            units.pop(idx)
    arr, ex, ey = rotate(arr, ex, ey)

print(ans)
print(ex+1, ey+1, end=' ')