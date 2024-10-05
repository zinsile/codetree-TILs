# step1. 직사각형 시계방향 회전
#     1.1 왼쪽상단 모서리 temp값에 저장
#     1.2 왼쪽 모서리 열 위로 shift
#     1.3 아래 모서리 열 왼쪽으로 shift
#     1.4 오른쪽 모서리열 아래로 shift
#     1.5 위에 모서리열 오른쪽으로 shift
#     1.6 왼쪽 상단 모서리 오른쪽 a값에 temp 넣기
# step2. 직사각형 영역 내 숫자들 평균으로 변환
#     2.1 a에서 평균 구해서 temp_a 에 평균 저장(자기자신,상,하,좌,우 범위 안에 있는지 확인)
#     2.2 temp_a 평균값들 a로 이동

n,m,q = map(int, input().split())
a = [[0 for _ in range(m+1)] for _ in range(n+1)]
temp_a = [[0 for _ in range(m+1)] for _ in range(n+1)]

def rotation(start_x,start_y,end_x,end_y):
    # 1.1 왼쪽 상단 모서리 temp값에 저장
    temp = a[start_x][start_y]
    # 1.2 왼쪽 모서리 열 위로 shift
    for i in range(start_y,end_x):
        a[i][start_y] = a[i+1][start_y]
    # 1.3 아래 모서리 열 왼쪽으로 shift
    for i in range(start_y,end_y):
        a[end_x][i] = a[end_x][i+1]
    # 1.4 오른쪽 모서리열 아래로 shift
    for i in range(end_x,start_x,-1):
        a[i][end_y] = a[i-1][end_y]
    # 1.5 위에 모서리열 오른쪽으로 shift
    for i in range(end_y,start_y,-1):
        a[start_x][i] = a[start_x][i-1]
    # 1.6 왼쪽 상단 모서리 오른쪽 a값에 temp 넣기
    a[start_x][start_y+1] = temp

def in_range(x,y):
    return x>=1 and x<n+1 and y>=1 and y<m+1

def average(x,y):
    dxs, dys = [0, 1, -1, 0, 0], [0, 0, 0, 1, -1]
    avg_list = [
                a[x+dx][y+dy]
                for dx,dy in zip(dxs, dys)
                if in_range(x+dx,y+dy)
                ]
    return sum(avg_list)//len(avg_list)

def set_average(start_x,start_y,end_x,end_y):
    dxs, dys = [0,1,-1,0,0], [0,0,0,1,-1]
    # 2.1 a에서 평균 구해서 temp_a 에 평균 저장(자기자신,상,하,좌,우 범위 안에 있는지 확인)
    for i in range(start_x,end_x+1):
        for j in range(start_y, end_y+1):
            temp_a[i][j] = average(i,j)
    # 2.2 temp_a 평균값들 a로 이동
    for i in range(start_x, end_x + 1):
        for j in range(start_y, end_y + 1):
            a[i][j] = temp_a[i][j]
    

def simulate(start_x,start_y,end_x,end_y):
    # step1. 직사각형 시계방향 회전
    rotation(start_x,start_y,end_x,end_y)
    # step2. 직사각형 영역 내 숫자들 평균으로 변환
    set_average(start_x,start_y,end_x,end_y)

for row in range(1,n+1):
    arr = list(map(int,input().split()))
    for col,elem in enumerate(arr,start=1):
        a[row][col] = elem

for _ in range(q):
    r1,c1,r2,c2 = map(int, input().split())
    simulate(r1,c1,r2,c2)

for row in a[1:]:
    for elem in row[1:]:
        print(elem, end=' ')
    print()