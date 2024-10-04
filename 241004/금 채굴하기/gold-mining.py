n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

def get_gold_cnt(row, col):
    max_cnt = 0
    for k in range(2*(n-1)+1):
        cnt = 0
        for i in range(n):
            for j in range(n):
                if abs(row-i)+abs(col-j)>k:
                    continue
                cnt += graph[i][j]
        if k*k+(k+1)*(k+1) <= cnt * m:
            max_cnt = max(max_cnt, cnt)
    return max_cnt

max_gold = 0
for row in range(n):
    for col in range(n):
        gold_cnt = get_gold_cnt(row,col)
        max_gold = max(max_gold, gold_cnt)

print(max_gold)