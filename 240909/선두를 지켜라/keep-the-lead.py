MAX_T = 10**6
n,m = map(int, input().split())
time_a, time_b = [0]*(MAX_T+1), [0]*(MAX_T+1)
pos_a,pos_b = 1,1

for _ in range(n):
    v,t = map(int, input().split())
    for i in range(t):
        time_a[pos_a] = time_a[pos_a-1]+v
        pos_a += 1

for _ in range(m):
    v,t = map(int, input().split())
    for i in range(t):
        time_b[pos_b] = time_b[pos_b-1]+v
        pos_b += 1

leader = 0 #1:a선두,2:b선두
cnt = 0
for i in range(pos_a+1):
    if time_a[i] == time_b[i]:
        continue
    elif time_a[i]>time_b[i]:
        if leader == 2:
            cnt += 1
            leader = 1
        else: leader = 1
    elif time_a[i]<time_b[i]:
        if leader == 1:
            cnt +=1
            leader=2
        else: leader=2

print(cnt)