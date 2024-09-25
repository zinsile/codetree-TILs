n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

s = 0
for i1 in range(n):
    for i2 in range(i1+1, n):
        for i3 in range(i2+1,n):
            x1,y1 = arr[i1][0],arr[i1][1]
            x2,y2 = arr[i2][0],arr[i2][1]
            x3,y3 = arr[i3][0],arr[i3][1]
            if (x1==x2 or x2==x3) and (y1==y2 or y2==y3):
                max_x,max_y = max(x1,x2,x3), max(y1,y2,y3)
                min_x,min_y = min(x1,x2,x3), min(y1,y2,y3)
                t = (max_x-min_x) * (max_y-min_y)
            else:
                t = 0
            s = max(s, t)
print(s)