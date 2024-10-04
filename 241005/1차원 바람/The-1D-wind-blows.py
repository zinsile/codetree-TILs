n,m,q = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
winds = [list(map(str, input().split())) for _ in range(q)]

def move_arr(row,dirc):
    if dirc == 0:
        temp = arr[row][m-1]
        for i in range(m-1,0,-1):
            arr[row][i] = arr[row][i-1]
        arr[row][0] = temp
    else:
        temp = arr[row][0]
        for i in range(0,m-1):
            arr[row][i] = arr[row][i+1]
        arr[row][m-1] = temp

def matching_rows(r1,r2):
    for i in range(m):
        if arr[r1][i] == arr[r2][i]:
            return True
    return False

for row, dirc in winds:
    row = int(row)-1
    if dirc == 'L':
        dic = 0
    else: dic = 1
    move_arr(row, dic)
    for row2 in range(row-1,-1,-1):
        if not matching_rows(row2,row2+1):
            break
        move_arr(row2, dic ^ 1)
        dic = dic ^ 1
    if dirc == 'L':
        dic = 0
    else: dic = 1
    for row3 in range(row+1,n):
        if not matching_rows(row3, row3-1):
            break
        move_arr(row3, dic ^ 1)
        dic = dic ^ 1

for rowlist in arr:
    for elem in rowlist:
        print(elem, end=' ')
    print()