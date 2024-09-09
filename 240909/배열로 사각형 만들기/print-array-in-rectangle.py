graph = [[0 for _ in range(5)] for _ in range(5)]

for i in range(5):
    graph[0][i] = 1
    graph[i][0] = 1

for i in range(1,5):
    for j in range(1,5):
        graph[i][j] = graph[i-1][j]+graph[i][j-1]

for raw in graph:
    for elem in raw:
        print(elem, end=' ')
    print()