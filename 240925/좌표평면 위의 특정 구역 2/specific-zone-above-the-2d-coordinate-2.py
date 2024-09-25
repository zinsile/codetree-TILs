MAX_N = 40000
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

square = MAX_N * MAX_N

for i in range(n):
    max_x,max_y = 0,0
    min_x,min_y = MAX_N, MAX_N
    
    for j in range(n):
        if i==j : continue

        x,y = arr[j][0], arr[j][1]
        max_x, max_y = max(max_x, x), max(max_y, y)
        min_x, min_y = min(min_x, x), min(min_y, y)
    square = min(square, (max_x-min_x)*(max_y-min_y))

print(square)