n = int(input())
graph = [
    list(map(int, input().split()))
    for _ in range(n)
]

def calculate(r,c,w,h):
    score = 0
    H,W= 0,0
    if h==1:
        H=1
    if w==1:
        W=1
    if h>1:
        H=h-1
    if w>1:
        W=w-1
    for _ in range(W):
        score += graph[r-1][c+1]
        r,c = r-1,c+1
    for _ in range(H):
        score += graph[r-1][c-1]
        r,c = r-1,c-1
    for _ in range(W):
        score += graph[r+1][c-1]
        r,c = r+1,c-1
    for _ in range(H):
        score += graph[r+1][c+1]
        r,c = r+1,c+1
    return score

def square(i, j):
    max_score = 0
    for k in range(2,n+1):
        for w in range(1,n):
            h = k-w
            if h==0:
                continue
            H,W= 0,0
            if h==1:
                H=1
            if w==1:
                W=1
            if h>1:
                H=h-1
            if w>1:
                W=w-1
            if i-(W)<0 or i-(W)>=n or j+(W)<0 or j+(W)>=n:
                continue
            if i-(W)-H<0 or i-(W)-H>=n or j+(W)-H<0 or j+(W)-H>=n:
                continue
            if i-H<0 or i-H>=n or j-H<0 or j-H>=n:
                continue
            score = calculate(i,j,w,h)
            max_score = max(max_score, score)
    return max_score

max_result = 0
for row in range(n):
    for col in range(n):
        result = square(row, col)
        max_result = max(max_result, result)

print(max_result)