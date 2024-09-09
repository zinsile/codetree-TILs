n = int(input())
cnt = 1
max_cnt = -1
x_num = -1
for i in range(n):
    num = int(input())
    if i == 0:
        max_cnt = max(max_cnt,cnt)
        x_num = num
        continue
    elif x_num == num:
        cnt += 1
        max_cnt = max(max_cnt,cnt)
        x_num = num
    elif x_num !=num:
        cnt = 1
        x_num = num

print(max_cnt)