n = int(input())
graph = [
    list(map(int, input().split()))
    for _ in range(n)
]

def in_range(x,y):
    return x>=0 and x<n and y>=0 and y<n


def get_score(x,y,w,h):
    move_nums = [w,h,w,h]
    dxs,dys = [-1,-1,1,1],[1,-1,-1,1]
    score = 0

    for num,dx,dy in zip(move_nums,dxs,dys):
        for n in range(num):
            if not in_range(x+dx,y+dy):
                return 0
            x, y = x+dx, y+dy
            score += graph[x][y]
    return score

ans = 0
for i in range(n):
    for j in range(n):
        for w in range(1,n):
            for h in range(1,n):
                ans = max(ans,get_score(i,j,w,h))

print(ans)