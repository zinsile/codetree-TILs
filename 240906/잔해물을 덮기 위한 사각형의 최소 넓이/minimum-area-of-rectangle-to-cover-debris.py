info = [list(map(int, input().split())) for _ in range(2)]
graph = [[0 for _ in range(2000)] for _ in range(2000)]

for t,(x1,y1,x2,y2) in enumerate(info):
    x,y = 1000,1000
    if t == 1:
        for i in range(x1,x2):
            for j in range(y1,y2):
                graph[x+i][y+j] -= 1
    else:
        for i in range(x1,x2):
            for j in range(y1,y2):
                graph[x+i][y+j] += 1

minx,miny = 2000,2000
maxx,maxy = 0,0

for i in range(2000):
    for j in range(2000):
        if graph[i][j] != 1:
            continue
        elif minx>=i and miny>=j:
            minx,miny = i,j
        elif maxx<=i and maxy<=j:
            maxx,maxy = i,j

cnt=0
for _ in range(minx,maxx+1):
    for _ in range(miny,maxy+1):
        cnt+=1

print(cnt)