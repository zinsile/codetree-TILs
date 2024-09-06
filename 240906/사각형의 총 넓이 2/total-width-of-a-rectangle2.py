n = int(input())
info = [list(map(int, input().split())) for _ in range(n)]
graph = [[0 for _ in range(200)] for _ in range(200)]
x,y = 100,100

for x1,y1,x2,y2 in info:
    for dx in range(x1,x2):
        for dy in range(y1,y2):
            graph[x+dx][y+dy] += 1

cnt = 0
for i in range(200):
    for j in range(200):
        if graph[i][j] > 0:
            cnt += 1
print(cnt)