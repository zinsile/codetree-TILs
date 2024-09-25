MAX_NUM = 1000
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dis = MAX_NUM*MAX_NUM*2
for i in range(n):
    for j in range(i+1,n):
        x1,y1 = arr[i][0], arr[i][1]
        x2,y2 = arr[j][0], arr[j][1]
        dis = min(dis, (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))

print(dis)