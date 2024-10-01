n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

def cnt_graph(r1,r2,c1,c2):
    cnt = 0
    for i in range(r1, r2+1):
        for j in range(c1, c2+1):
            cnt += graph[i][j]
    return cnt

max_cnt = 0
for r in range(n):
    for c in range(n):
        if r+2>=n or c+2>=n:
            continue
        cnt = cnt_graph(r,r+2,c,c+2)
        max_cnt = max(max_cnt, cnt)

print(max_cnt)