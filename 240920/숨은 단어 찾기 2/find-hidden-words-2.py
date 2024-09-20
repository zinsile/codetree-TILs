n,m = map(int, input().split())

arr = [list(input()) for _ in range(n)]

def in_range(x,y):
    return x>=0 and x<n and y>=0 and y<m

dxs,dys = [-1,-1,-1,0,1,1,1,0], [-1,0,1,1,1,0,-1,-1]

cnt = 0

for i in range(n):
    for j in range(m):

        if arr[i][j] != 'L':
            continue
        
        for dx,dy in zip(dxs,dys):
            curt = 0
            curx = i
            cury = j
            while True:
                nx = curx + dx
                ny = cury + dy
                if not in_range(nx,ny):
                    break
                if arr[nx][ny] != 'E':
                    break
                curt += 1
                curx = nx
                cury = ny
            if curt >= 2:
                cnt += 1

print(cnt)