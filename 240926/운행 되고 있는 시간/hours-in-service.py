n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

max_time = 0
for i in range(n):
    time = [0]*1001
    for j in range(n):
        if i==j:
            continue
        s,e = arr[j]
        for k in range(s,e):
            if time[k]==0:
                time[k] = 1
    max_time = max(max_time,sum(time))
print(max_time)