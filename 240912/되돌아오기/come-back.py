n = int(input())
mapper = {'N':0,'E':1,'S':2,'W':3}
dxs, dys = [-1,0,1,0],[0,1,0,-1]
x,y = 0,0
time = 1
end = False

for _ in range(n):
    d,t = input().split()
    dir_num = mapper[d]
    for _ in range(int(t)):
        x,y = x+dxs[dir_num], y+dys[dir_num]
        if x==0 and y==0 and not end:
            print(time)
            end = True
            break
        time+=1
if not end:
    print(-1)