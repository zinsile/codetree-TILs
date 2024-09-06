info = [list(map(int, input().split())) for _ in range(3)]
graph = [[0 for _ in range(2000)] for _ in range(2000)]

for t,(x1,y1,x2,y2) in enumerate(info):
    x,y = 1000,1000
    if t == 2:
        for i in range(x1,x2):
            for j in range(y1,y2):
                graph[x+i][y+j] -= 1
    else:
        for i in range(x1,x2):
            for j in range(y1,y2):
                graph[x+i][y+j] += 1

cnt = 0
for i in range(2000):
    for j in range(2000):
        if graph[i][j] == 1:
            cnt+=1

print(cnt)