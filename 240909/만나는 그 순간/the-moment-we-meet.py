n,m = map(int, input().split())
a_comm = [list(map(str, input().split())) for _ in range(n)]
b_comm = [list(map(str, input().split())) for _ in range(m)]

a_pos = [0]*1000
b_pos = [0]*1000
dis,p = 0,0
for d,t in a_comm:
    t = int(t)
    for i in range(t):
        if d=='L':
            dis = dis-1
            a_pos[p+i+1] = dis
        else:
            dis = dis+1
            a_pos[p+i+1] = dis
    p = p+t
dis,p = 0,0
for d,t in b_comm:
    t = int(t)
    for i in range(t):
        if d=='L':
            dis = dis-1
            b_pos[p+i+1] = dis
        else:
            dis = dis+1
            b_pos[p+i+1] = dis
    p = p+t

for i in range(1,1001):
    if a_pos[i] == b_pos[i]:
        print(i)
        break