n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

ans = 0
M = n//2

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def bfs(i,j,v):
    q = []

    q.append((i,j))
    group[-1].add((i,j))
    v[i][j] = 1

    while q:
        x,y = q.pop(0)
        for nx, ny in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
            if in_range(nx, ny) and v[nx][ny]==0 and arr[x][y]==arr[nx][ny]:
                q.append((nx, ny))
                group[-1].add((nx,ny))
                v[nx][ny] = 1 


for k in range(4):
    group = []
    nums = []
    # [1] 예술점수 구하기: 그룹나누고, 가능한 두 개 그룹의 점수 누적
    v = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if v[i][j] == 0:
                group.append(set())
                nums.append(arr[i][j])
                bfs(i,j,v)
    # [1-2] 각 그룹간 점수 계산(누적)
    CNT = len(nums)
    for i in range(CNT-1):
        for j in range(i+1, CNT):
            point = (len(group[i]) + len(group[j])) * nums[i] * nums[j]
            for x, y in group[i]:
                for nx,ny in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                    if (nx, ny) in group[j]:
                        ans += point

    if k==3:
        break
    
    # [2] 회전시키기: '+'반시계 회전, 부분사각형 시계방향
    narr = [[0]*n for _ in range(n)]

    for i in range(n):
        narr[M][i] = arr[i][M]
        narr[i][M] = arr[M][n-i-1]
    for sx,sy in [(0,0),(M+1,0),(0,M+1),(M+1,M+1)]:
        for i in range(M):
            for j in range(M):
                narr[sx+i][sy+j] = arr[sx+M-j-1][sy+i]
    arr = narr

print(ans)