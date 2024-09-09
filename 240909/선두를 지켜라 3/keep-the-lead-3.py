n,m = map(int, input().split())
pos_a,pos_b = [0]*(10**6+1), [0]*(10**6+1)
time_a,time_b = 1,1

for _ in range(n):
    v,t = map(int, input().split())
    for i in range(t):
        pos_a[time_a] = pos_a[time_a-1]+v
        time_a += 1

for _ in range(m):
    v,t = map(int, input().split())
    for i in range(t):
        pos_b[time_b] = pos_b[time_b-1]+v
        time_b += 1

leader = 0  #1-a선두,2-b선두,3-공동선두
cnt = 0
for i in range(1,time_a):
    if pos_a[i]>pos_b[i]:
        if leader != 1:
            cnt += 1
            leader = 1
    elif pos_a[i]<pos_b[i]:
        if leader!=2:
            cnt += 1
            leader = 2
    elif pos_a[i] == pos_b[i]:
        if leader!=3:
            cnt+=1
            leader = 3
print(cnt)