n,m = map(int, input().split())
graph=[[0 for _ in range(m)] for _ in range(n)]

num = 0
for i in range(m):
    if i%2==0:
        for j in range(n):
            graph[j][i] = num
            num+=1
    else:
        for j in range(n-1,-1,-1):
            graph[j][i] = num
            num+=1

for raw in graph:
    for elem in raw:
        print(elem, end=' ')
    print()