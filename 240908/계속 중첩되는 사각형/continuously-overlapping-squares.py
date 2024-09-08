n = int(input())
info = [list(map(int, input().split())) for _ in range(n)]

graph = [[0 for _ in range(200)] for _ in range(200)]

#빨간-1, 파란-2
for i,(x1,y1,x2,y2) in enumerate(info):
    if i%2==0:
        color = 1
    else:
        color = 2
    x,y = 100,100
    for dx in range(x1,x2):
        for dy in range(y1,y2):
            graph[x+dx][y+dy] = color

cnt = 0
for i in range(200):
    for j in range(200):
        if graph[i][j] == 2:
            cnt+=1

print(cnt)