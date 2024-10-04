import sys

n,m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

def in_range(x,y):
    return x>=0 and x<n and y>=0 and y<m

def make_rect(x1,y1,x2,y2,w1,h1,w2,h2):
    tmp = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(x1,x1+h1+1):
        for j in range(y1,y1+w1+1):
            if not in_range(i,j):
                return False
            tmp[i][j] = 1
    for k in range(x2,x2+h2+1):
        for l in range(y2,y2+w2+1):
            if not in_range(k,l):
                return False
            if tmp[k][l] == 1:
                return False
    return True

def get_score(x,y,w,h):
    return sum([
        graph[i][j]
        for i in range(x,x+h+1)
        for j in range(y,y+w+1)
    ])

def cal_area(i,j,k,l):
    max_score = -sys.maxsize
    for w1 in range(m):
        for h1 in range(n):
            for w2 in range(m):
                for h2 in range(n):
                    if not make_rect(i,j,k,l,w1,h1,w2,h2):
                        continue
                    max_score = max(max_score, get_score(i,j,w1,h1)+get_score(k,l,w2,h2))
    return max_score

ans = -sys.maxsize
for i in range(n):
    for j in range(m):
        for k in range(n):
            for l in range(m):
                if i==k and j==l:
                    continue
                ans = max(ans, cal_area(i,j,k,l))

print(ans)