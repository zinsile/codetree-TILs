n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

result = 0
for i in range(n):# 가로
    prev = graph[i][0]
    cnt = 0
    max_cnt = 0
    for j in range(n):
        max_cnt = max(max_cnt,cnt)
        if prev == graph[i][j]:
            cnt += 1
        if prev != graph[i][j]:
            prev = graph[i][j]
            cnt = 1
    if max_cnt >= m:
        result += 1
    
    prev = graph[0][i]
    cnt = 0
    max_cnt= 0
    for j in range(n):
        max_cnt = max(max_cnt,cnt)
        if prev == graph[j][i]:
            cnt += 1
        if prev != graph[j][i]:
            prev = graph[j][i]
            cnt = 1
    if max_cnt >= m:
        result += 1

print(result)