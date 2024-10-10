L, N, Q = map(int, input().split()) # 체스판, 기사 수, 명령 수
arr = [[2]*(L+2)]+ [[2]+list(map(int, input().split()))+[2] for _ in range(L)] + [[2]*(L+2)]
person = [[0]*5] + [list(map(int, input().split())) for _ in range(N)] # x,y,h,w,k
unit = [list(map(int, input().split())) for _ in range(Q)]

live = [True]*(N+1)
damage = [0]*(N+1) # 초기 체력으로 업데이트 되어있음 damage[i]=0 이면 죽음
dxs, dys = [-1,0,1,0], [0,1,0,-1]

# pos_arr은 기사 위치만 표시되어있음 (함정, 벽 -> arr)
pos_arr = [[2]*(L+2)]+[[2]+[0]*L+[2] for _ in range(L)]+[[2]*(L+2)]
for i, (x,y,h,w,k) in enumerate(person[1:], start=1):
    damage[i] = k
    for dx in range(h):
        for dy in range(w):
            pos_arr[x+dx][y+dy] = i
ans = 0

def moving(idx, d, pos_arr, arr):
    global person, dxs, dys
    q = []
    q.append(idx)
    flag = 0 # 벽 만나면 1
    temp = []
    temp.append(idx)

    while q:
        id = q.pop(0)
        x,y,h,w,k = person[id]
        for i in range(h):
            for j in range(w):
                nx, ny = (x+i)+dxs[d], (y+j)+dys[d]
                if arr[nx][ny] == 2:
                    flag = 1
                    return temp, flag
                elif pos_arr[nx][ny] != id and pos_arr[nx][ny]>0 and not pos_arr[nx][ny] in temp:
                    q.append(pos_arr[nx][ny])
                    temp.append(pos_arr[nx][ny])
    return temp, flag
cnt=0
for idx, d in unit:
    cnt+=1
    if not live[idx]:
        continue
    moved_p, flag = moving(idx, d, pos_arr, arr)
    # 벽 있어서 이동 못한 경우 대미지 입지 않음
    if flag == 1:
        continue
    # 밀린애들과 안밀린애들 새로운 position 업데이트
    npos_arr = [[2]*(L+2)]+[[2]+[0]*L+[2] for _ in range(L)]+[[2]*(L+2)]
    for x in range(1,L+1):
        for y in range(1,L+1):
            if pos_arr[x][y] in moved_p:
                npos_arr[x+dxs[d]][y+dys[d]] = pos_arr[x][y]
            elif not pos_arr[x][y] in moved_p and pos_arr[x][y]>0:
                npos_arr[x][y] = pos_arr[x][y]
    pos_arr = npos_arr
    
    for x in range(1,L+1):
        for y in range(1,L+1):
            if pos_arr[x][y] == 0:
                continue
            # 명령받은 기사 아니고 & 함정있다면 : 대미지 -= 1
            if pos_arr[x][y] != idx and arr[x][y] == 1:
                damage[pos_arr[x][y]] -= 1
                ans += 1
    # 체스판에서 사라질 기사 있는지 확인
    for id, t in enumerate(damage[1:], start=1):
        if t <= 0:
            live[id] = False

print(ans)