R,C,K = map(int, input().split())
unit = [list(map(int, input().split())) for _ in range(K)]

arr = [[1]+[0]*C+[1] for _ in range(R+3)]+[[1]*(C+2)]
exit = set()
num = 2
dxs, dys = [-1,0,1,0], [0,1,0,-1]
ans = 0

def bfs(arr,exit,i,j):
    q = []
    v = [[False]*(C+2) for _ in range(R+4)]
    max_row = 0

    q.append((i,j))
    v[i][j] = True
    while q:
        x,y = q.pop(0)
        max_row = max(max_row, x)
        # 네방향, 미방문, 조건:현재와 다음의 arr 값 동일 or 현재가 탈출구 다음이 다른골렘
        for dx,dy in zip(dxs, dys):
            nx, ny = x+dx, y+dy
            if not v[nx][ny] \
                    and (arr[x][y]==arr[nx][ny] or (arr[nx][ny]>1 and (x,y) in exit)):
                q.append((nx,ny))
                v[nx][ny] = True
    return max_row

for cj, d in unit:
    ci = 1
    # [1] 골램 이동
    while True:
        # 남쪽으로 한칸 내리기
        if arr[ci+2][cj]==0 and arr[ci+1][cj-1]==0 and arr[ci+1][cj+1]==0:
            ci += 1
        # 남쪽 안될시 서쪽으로 회전하고 한칸 내리기 & 탈출구 반시계 회전
        elif arr[ci-1][cj-1]==0 and arr[ci][cj-2]==0 \
                and arr[ci+1][cj-1]==0 and arr[ci+1][cj-2]==0 and arr[ci+2][cj-1]==0:
            ci += 1
            cj -= 1
            d = (d+3)%4
        # 남쪽 안될시 동쪽으로 회전하고 한칸 내리기 & 탈출구 시계 회전
        elif arr[ci-1][cj+1]==0 and arr[ci][cj+2]==0 \
                and arr[ci+1][cj+1]==0 and arr[ci+1][cj+2]==0 and arr[ci+2][cj+1]==0:
            ci += 1
            cj += 1
            d = (d+1)%4
        # 남,서,동 모두 못가면 종료
        else:
            break

    # 골렘이 범위밖에 위치한다면
    if ci<4:
        arr = [[1] + [0] * C + [1] for _ in range(R + 3)] + [[1] * (C + 2)]
        exit = set()
        num = 2
        continue
    else:
        arr[ci][cj] = num
        for dx, dy in zip(dxs, dys):
            nx, ny = ci+dx, cj+dy
            arr[nx][ny] = num
        exit.add((ci+dxs[d],cj+dys[d]))
        num += 1

    # [2] 정령이동
    row = bfs(arr,exit,ci,cj)
    ans += (row-2)

print(ans)