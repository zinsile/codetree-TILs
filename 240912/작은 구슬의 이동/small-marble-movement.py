n,t = map(int,input().split())
r,c,d = map(str, input().split())

def in_range(x,y):
    return x>=1 and x<n+1 and y>=1 and y<n+1

dxs, dys = [0,1,-1,0],[1,0,0,-1]

mapper = {
    'R':0,
    'D':1,
    'U':2,
    'L':3
}

x,y = int(r),int(c)
dir_num = mapper[d]

for _ in range(t):
    nx,ny = x+dxs[dir_num], y+dys[dir_num]
    if not in_range(nx,ny):
        dir_num = 3-dir_num
        continue
    x, y = nx, ny

print(x,y,end= ' ')