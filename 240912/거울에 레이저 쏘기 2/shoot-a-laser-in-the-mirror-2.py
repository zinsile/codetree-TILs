n = int(input())
graph =[list(input()) for _ in range(n)]
number = int(input())
dxs,dys = [1,0,-1,0],[0,-1,0,1]

#'\':dir_num = (dir_num-1+4)%4, '/':dir_num = (dir_num+1)%4

if (number//n)==0:
    r,c = 0,number%n-1
    dir_num = 0
elif (number//n)==1 and number%3==0:
    r,c = 0,n-1
    dir_num = 0
elif (number//n)==1 and number%3!=0:
    r,c = number%n-1,n-1
    dir_num = 1
elif (number//n)==2 and number%3==0:
    r,c = n-1,n-1
    dir_num = 1
elif (number//n)==2 and number%3!=0:
    r,c = n-1,n-(number%n)
    dir_num = 2
elif (number//n)==3 and number%3==0:
    r,c = n-1,0
    dir_num = 2
elif (number//n)==3 and number%3!=0:
    r,c = n-(number%n),0
    dir_num = 3
elif (number//n)==4 and number%3==0:
    r,c = 0,0
    dir_num = 3

def in_range(x,y):
    return x>=0 and x<n and y>=0 and y<n

res = 1
while True:
    if graph[r][c] == "/" :
        dir_num = (dir_num-1+4)%4
    else:
        dir_num = (dir_num+1)%4
    
    nx,ny = r+dxs[dir_num], c+dys[dir_num]
    if not in_range(nx,ny):
        break
    res+=1
    r,c = nx,ny
print(res)