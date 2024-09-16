r,c = map(int, input().split())
graph = [list(input().split()) for _ in range(r)]

cnt = 0
for i in range(1,r-1):
    for j in range(1,c-1):
        for k in range(i+1,r-1):
            for l in range(j+1,c-1):
                if graph[i][j]!=graph[0][0] and graph[k][l]!=graph[r-1][c-1]:
                    cnt+=1

if graph[0][0] == graph[r-1][c-1]:
    print(0)
else:print(cnt)