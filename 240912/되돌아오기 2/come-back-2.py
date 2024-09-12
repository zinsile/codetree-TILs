comm = list(input())
time = 1
dxs, dys = [-1,0,1,0],[0,1,0,-1]
dir_num = 0
end = False
x,y = 0,0

for c in comm:
    if c=='L':
        dir_num = (dir_num-1+4)%4
    elif c=='R':
        dir_num = (dir_num+1)%4
    else:
        x,y = x+dxs[dir_num], y+dys[dir_num]
    time += 1
    if x==0 and y==0 and not end:
        print(time-1)
        end = True
        break
if not end:
    print(-1)