MAX = 10**6
n,m = map(int, input().split())
pos_a,pos_b = [0]*(MAX+1), [0]*(MAX+1)  #pos_a[t]:t초일때 a의 위치
present_a,present_b = 1,1 #현재 시간

for _ in range(n):
    t,d = map(str, input().split())
    t = int(t)
    for i in range(t):
        if d=='L':
            pos_a[present_a] = pos_a[present_a-1] -1
            present_a += 1
        else:
            pos_a[present_a] = pos_a[present_a-1] +1
            present_a += 1

for _ in range(m):
    t,d = map(str, input().split())
    t = int(t)
    for i in range(t):
        if d=='L':
            pos_b[present_b] = pos_b[present_b-1] -1
            present_b += 1
        else:
            pos_b[present_b] = pos_b[present_b-1] +1
            present_b += 1

#먼저 끝난 로봇은 다른 로봇이 끝나기 전까지 같은 위치로 설정
for i in range(abs(present_a-present_b)):
    if present_a>present_b:
        pos_b[present_b+i+1] = pos_b[present_b]
    elif present_a<present_b:
        pos_a[present_a+i+1] = pos_a[present_a]

samepos = True
cnt = 0
for i in range(1,max(present_a,present_b)+1):
    if pos_a[i]==pos_b[i]:
        if not samepos:
            cnt += 1
            samepos = True
        elif samepos:
            samepos = True
    else:
        samepos = False

print(cnt)