import sys
n = int(input())
check = [list(map(int, input().split())) for _ in range(n)]
min_int = sys.maxsize

def cal_dis(check):
    dsum = 0
    for i in range(n-1):
        dsum += (abs(check[i][0]-check[i+1][0]) + abs(check[i][1]-check[i+1][1]))
    return dsum

for i in range(1,n-1):
    x,y = check[i][0],check[i][1]
    check[i][0],check[i][1] = check[i-1][0],check[i-1][1]
    dsum = cal_dis(check)
    min_int = min(min_int, dsum)
    check[i][0],check[i][1] = x,y

print(min_int)