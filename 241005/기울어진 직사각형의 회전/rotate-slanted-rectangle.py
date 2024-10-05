n = int(input())
a = [[0 for _ in range(n+1)] for _ in range(n+1)]

for row in range(1,n+1):
    for col,elem in enumerate(list(map(int, input().split())), start=1):
        a[row][col] = elem

r, c, m1, m2, m3, m4, dirc = map(int, input().split())

def rotate(r, c, m1, m2, m3, m4, dirc):
    # <dirc 0 인 경우 반시계>
    if dirc == 0:
        move_nums = [m4,m3,m2,m1]
        dxs, dys = [-1,-1,1,1], [-1,1,1,-1]
    else:
        move_nums = [m1,m2,m3,m4]
        dxs, dys = [-1,-1,1,1], [1,-1,-1,1]
    
    for num, dx,dy in zip(move_nums, dxs, dys):
        for _ in range(num):
            a[r][c] = a[r+dx][c+dy]
            r, c = r+dx, c+dy


def simulate(r, c, m1, m2, m3, m4, dirc):
    # step1. a[r][c] = temp에 저장
    temp = a[r][c]
    
    # step2. 직사각형 회전
    rotate(r, c, m1, m2, m3, m4, dirc)
    
    # step3. dirc == 0 : a[r-1][c+1] = temp
    if dirc == 0:
        a[r-1][c+1] = temp
    #             == 1 : a[r-1][c-1] = temp
    else:
        a[r-1][c-1] = temp

simulate(r, c, m1, m2, m3, m4, dirc)

for row in a[1:]:
    for elem in row[1:]:
        print(elem, end = ' ')
    print()