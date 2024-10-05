n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())
temp = [[0 for _ in range(n)] for _ in range(n)]

def in_range(x,y):
    return x>=0 and x<n and y>=0 and y<n

def bomb(x,y):
    
    t = graph[x][y]
    graph[x][y] = 0
    
    dxs,dys = [0,0,-1,1],[1,-1,0,0]
    for dx,dy in zip(dxs, dys):
        for i in range(t-1):
            if not in_range(x+(dx*(i+1)), y+(dy*(i+1))):
                continue
            graph[x+(dx*(i+1))][y+(dy*(i+1))] = 0

def grav():
    for c in range(n-1,-1,-1):
        temp_row = n-1
        for r in range(n-1,-1,-1):
            if graph[r][c] > 0:
                temp[temp_row][c] = graph[r][c]
                temp_row -= 1

        

def simulate():
    
    # step1. graph에서 폭탄 터치기
    bomb(r-1,c-1)
    
    # step2. 중력작용 -> temp 만들어서 temp에 값 옮기고 나중에 temp출력
    grav()

simulate()

for row in temp:
    for elem in row:
        print(elem, end =' ')
    print()