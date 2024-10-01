n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

block = [[(0,-1),(0,1)],[(-1,0),(1,0)],[(1,0),(0,1)],[(0,-1),(1,0)],[(-1,0),(0,-1)],[(-1,0),(0,1)]]

def in_range(x,y):
    return x>=0 and x<n and y>=0 and y<m

max_score = 0
for i in range(n):
    for j in range(m):
        for b in block:
            score = graph[i][j]
            for cx,cy in b:
                if not in_range(i+cx,j+cy):
                    break
                score += graph[i+cx][j+cy]
            max_score = max(max_score, score)

print(max_score)