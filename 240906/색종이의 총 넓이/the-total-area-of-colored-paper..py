n = int(input())
colorp = [list(map(int, input().split())) for _ in range(n)]
graph = [[0 for _ in range(200)] for _ in range(200)]
ox,oy = 100,100

for x,y in colorp:
    for i in range(x,x+8):
        for j in range(y,y+8):
            graph[ox+i][oy+j] += 1

cnt = 0
for i in range(200):
    for j in range(200):
        if graph[i][j] > 0:
            cnt+=1

print(cnt)