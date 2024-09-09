n = int(input())
graph = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    graph[0][i] = 1
    graph[i][0] = 1

for i in range(1,n):
    for j in range(1,n):
        graph[i][j] = graph[i-1][j-1] + graph[i-1][j] + graph[i][j-1]

for raw in graph:
    for elem in raw:
        print(elem, end=' ')
    print()