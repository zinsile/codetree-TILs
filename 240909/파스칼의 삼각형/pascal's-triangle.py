n = int(input())
graph = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    graph[i][0] = 1

for i in range(1,n):
    for j in range(1,n):
        graph[i][j] = graph[i-1][j-1] + graph[i-1][j]

for i in range(n):
    for j in range(n):
        if graph[i][j]==0:
            continue
        else: print(graph[i][j],end=' ')
    print()