k,n = map(int, input().split())
rank = [list(map(int, input().split())) for _ in range(k)]

result = 0
for i in range(1,n+1):
    for j in range(i+1,n+1):
        score = 0
        for l in range(k):
            if rank[l].index(i) < rank[l].index(j):
                score += 1
            elif rank[l].index(i) > rank[l].index(j):
                score -= 1
        if abs(score) == k:
            result += 1

print(result)