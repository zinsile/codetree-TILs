n = int(input())
graph = [[0 for _ in range(n)] for _ in range(n)]

num = 1
cnt = 0
for i in range(n-1,-1,-1):
    if cnt%2==0:
        for j in range(n-1,-1,-1):
            graph[j][i] = num
            num+=1
    else:
        for j in range(n):
            graph[j][i] = num
            num+=1
    cnt +=1

for raw in graph:
    for elem in raw:
        print(elem, end=' ')
    print()