n,m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

def in_range(x,y):
    return x>=0 and x<n and y>=0 and y<m 

def checking_subarea(x1,y1,x2,y2):
    return all([
        graph[i][j]>0
        for i in range(x1,x2+1)
        for j in range(y1,y2+1)
    ])

ans = -1
for i in range(n):
    for j in range(m):
        for k in range(i,n):
            for l in range(j,m):
                if checking_subarea:
                    ans = max(ans, (k-i+1)*(l-j+1))

print(ans)