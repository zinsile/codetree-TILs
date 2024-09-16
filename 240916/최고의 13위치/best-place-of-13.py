n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

max_coins = 0
for i in range(n):
    for j in range(n-2):
        max_coins = max(max_coins,graph[i][j]+graph[i][j+1]+graph[i][j+2])

print(max_coins)