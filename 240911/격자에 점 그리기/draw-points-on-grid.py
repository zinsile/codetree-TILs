n,m = map(int, input().split())
graph = [[0]*n for _ in range(n)]
for i in range(m):
    r,c = map(int, input().split())
    graph[r-1][c-1] = i+1

for raw in graph:
    for elem in raw:
        print(elem, end=' ') 
    print()