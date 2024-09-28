x,y = map(int, input().split())

max_num = 0
for i in range(x,y+1):
    arr = list(map(int, list(str(i))))
    max_num = max(max_num, sum(arr))

print(max_num)