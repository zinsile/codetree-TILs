n = int(input())
graph = [[0 for _ in range(n)] for _ in range(n)]

num=1
for i in range(n):
    for j in range(n):
        graph[j][i] = num
        num+=1

for raw in graph:
    for elem in raw:
        print(elem, end=' ')
    print()