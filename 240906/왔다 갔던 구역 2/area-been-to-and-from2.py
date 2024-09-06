n = int(input())
comm = [list(map(str, input().split())) for _ in range(n)]
move = [0]*200
x = 100
y = 100

for k, t in comm:
    k = int(k)
    if t=='R':
        y = x + k
    else:
        y = x - k
    if x<y:
        a,b=x,y
    else: b,a=x,y
    for i in range(a,b):
        move[i] += 1
    x = y

cnt = 0
for i in move:
    if i > 1:
        cnt+=1

print(cnt)