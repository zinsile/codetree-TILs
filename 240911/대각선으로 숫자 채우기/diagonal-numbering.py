n,m = map(int, input().split())
graph = [[0 for _ in range(m)] for _ in range(n)]

num = 1
for j in range(m):
    t = 0
    for i in range(0,j+1):
        if j==-1:
            continue
        graph[t][j] = num
        num+=1
        j -= 1
        t += 1

for j in range(1,n):
    t = j
    for i in range(0,j+1):
        if t==n:
            continue
        graph[t][n-1-i] = num
        num+=1
        t+=1

for raw in graph:
    for elem in raw:
        print(elem, end=' ')
    print()