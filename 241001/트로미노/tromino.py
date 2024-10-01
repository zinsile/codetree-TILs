n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

block = [[(0,-1),(0,1)],[(-1,0),(1,0)],[(1,0),(0,1)],[(0,-1),(1,0)],[(-1,0),(0,-1)],[(-1,0),(0,1)]]

def in_range(x,y):
    return x>=0 and x<n and y>=0 and y<m

def get_max_sum(x,y):
    max_get_score = 0
    for b in block:
            score = graph[x][y]
            for cx,cy in b:
                if not in_range(x+cx,y+cy):
                    break
                score += graph[x+cx][y+cy]
            max_get_score = max(max_get_score,score)
    return max_get_score
            

max_score = 0
for i in range(n):
    for j in range(m):
        score = get_max_sum(i,j)
        max_score = max(max_score, score)

print(max_score)