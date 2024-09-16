graph = [list(map(int, input().split())) for _ in range(19)]

winner,x,y = 0,0,0
for i in range(19):
    for j in range(19):
        if graph[i][j] == 0:
            continue
        cnt = 1
        #가로
        for k in range(1,5):
            if graph[i][j] == graph[i][j+k]:
                cnt += 1
        if cnt == 5:
            winner = graph[i][j]
            x,y = i+1,j+3
        else: cnt = 1
        #세로
        for k in range(1,5):
            if graph[i][j] == graph[i+k][j]:
                cnt += 1
        if cnt == 5:
            winner = graph[i][j]
            x,y = i+3,j+1
        else: cnt = 1
        #왼대각선
        for k in range(1,5):
            if i+k<19 and j+k<19 and graph[i][j] == graph[i+k][j+k]:
                cnt += 1
        if cnt == 5:
            winner = graph[i][j]
            x,y = i+3,j+3
        else: cnt = 1
        #오대각선
        for k in range(1,5):
            if i-k<19 and j-k<19 and graph[i][j] == graph[i-k][j-k]:
                cnt += 1
        if cnt == 5:
            winner = graph[i][j]
            x,y = i-1,j-1
print(winner)
print(x,y,end=' ')