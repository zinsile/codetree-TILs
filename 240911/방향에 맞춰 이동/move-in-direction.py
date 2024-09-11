n = int(input())
x,y= 0,0
dx,dy = [-1,0,0,1],[0,-1,1,0]
direction = ['W','S','N','E']

for _ in range(n):
    d,k = map(str, input().split())
    dirc = direction.index(d)
    x,y = x+dx[dirc]*int(k), y+dy[dirc]*int(k)

print(x,y,end=' ')