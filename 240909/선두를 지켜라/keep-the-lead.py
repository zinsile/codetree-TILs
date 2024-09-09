n,m = map(int, input().split())
a_moving = [list(map(int, input().split())) for _ in range(n)]
b_moving = [list(map(int, input().split())) for _ in range(m)]
a_pos,b_pos = [0]*10**6,[0]*10**6

ap,h = 0,0
for v,t in a_moving:
    for i in range(t):
        for j in range(v):
            a_pos[ap+j+1] = h+i+1
        ap = ap+v
    h = h+t

bp,h = 0,0
for v,t in b_moving:
    for i in range(t):
        for j in range(v):
            b_pos[bp+j+1] = h+i+1
        bp = bp+v
    h = h+t

first_runner = 'N'
cnt = 0
for i in range(1,10**6):
    if i > min(ap,bp):
        break
    elif a_pos[i] == b_pos[i]:
        continue
    elif a_pos[i]<b_pos[i] and (first_runner=='b'or first_runner=='N'):
        cnt+=1
        first_runner = 'a'
    elif a_pos[i]>b_pos[i] and (first_runner=='a'or first_runner=='N'):
        cnt += 1
        first_runner = 'b'
    # print(first_runner)
print(cnt-1)