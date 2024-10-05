n,m,q = map(int, input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
winds = [list(map(int,input().split())) for _ in range(q)]

def in_range(x,y):
    return x>=0 and x<n and y>=0 and y<m

def avg(x1,y1,x2,y2):
    temp = [[0 for _ in range(m)] for _ in range(n)]
    dxs,dys = [1,0,-1,0],[0,1,0,-1]
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            sum_nums = graph[i][j]
            nums_cnt = 1
            for dx,dy in zip(dxs,dys):
                if not in_range(i+dx,j+dy):
                    continue
                sum_nums += graph[i+dx][j+dy]
                nums_cnt += 1
            temp[i][j] = sum_nums//nums_cnt
    return temp

def moved(x1,y1,x2,y2):
    temp = [[-1 for _ in range(m)] for _ in range(n)]
    dxs,dys = [1,0,-1,0],[0,1,0,-1]
    move_nums = [x2-x1,y2-y1,x2-x1,y2-y1]
    for num,dx,dy in zip(move_nums, dxs, dys):
        for i in range(num):
            temp[x1][y1] = graph[x1+dx][y1+dy]
            x1,y1 = x1+dx,y1+dy
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            if temp[i][j] == -1:
                temp[i][j] = graph[i][j]
    return temp

def exchanged(temp,i,j,k,l):
    for x in range(i,k+1):
        for y in range(j,l+1):
            graph[x][y] = temp[x][y]


for x1,y1,x2,y2 in winds:
    temp_graph = moved(x1-1,y1-1,x2-1,y2-1)
    exchanged(temp_graph,x1-1,y1-1,x2-1,y2-1)
    temp_graph = avg(x1-1,y1-1,x2-1,y2-1)
    exchanged(temp_graph,x1-1,y1-1,x2-1,y2-1)

for row in graph:
    for elem in row:
        print(elem, end = ' ')
    print()