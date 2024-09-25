MAX_NUM = 100

n = int(input())
arr = [0] * (MAX_NUM + 1)

for _ in range(n):
    x, c = input().split()
    x = int(x)
    arr[x] = 1 if c == 'G' else 2

max_len = 0
for i in range(MAX_NUM + 1):
    for j in range(i+1, MAX_NUM + 1):

        if arr[i] == 0 or arr[j] == 0:
            continue
        
        cnt_g, cnt_h = 0, 0

        for k in range(i, j+1):
            if arr[k] == 1:
                cnt_g += 1
            if arr[k] == 2:
                cnt_h += 1
            
        if cnt_g == 0 or cnt_h == 0 or cnt_g == cnt_h:
            max_len = max(max_len, j-i)

print(max_len)