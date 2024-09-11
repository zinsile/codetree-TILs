arr = list(input())
dx,dy = [0,1,0,-1],[1,0,-1,0]
x,y = 0,0
dic_num = 0

for t in arr:
    if t=="F":
        x,y = x+dx[dic_num], y+dy[dic_num]
    elif t=="L":
        dic_num = (dic_num-1+4)%4
    elif t=="R":
        dic_num = (dir_num+1)%4

print(x,y,end=' ')