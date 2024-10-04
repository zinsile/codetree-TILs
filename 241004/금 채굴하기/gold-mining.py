n, m = map(int, input().split())
graph = [
    list(map(int, input().split())) 
    for _ in range(n)
]

def get_area(k):
    return k*k + (k+1)*(k+1)

def get_gold(r,c,k):
    cnt = sum([
        graph[i][j]
        for i in range(n)
        for j in range(n)
        if abs(r-i)+abs(c-j) <= k
    ])
    return cnt

max_gold = 0
for row in range(n):
    for col in range(n):
        for k in range(2*(n-1) + 1):
            gold_cnt = get_gold(row, col, k)

            if gold_cnt * m >= get_area(k):
                max_gold = max(max_gold, gold_cnt)

print(max_gold)