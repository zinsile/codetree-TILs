n,k,p,t = map(int, input().split())
sick = [0]*(n+1)    #감염여부 : 정상-0, 감염-1
infecting_cnt = [0]*(n+1)
hand_shake = [list(map(int, input().split())) for _ in range(t)]
hand_shake.sort()
sick[p] = 1

for t,x,y in hand_shake:
    if sick[x]==1 and sick[y]==1:
        infecting_cnt[x] += 1
        infecting_cnt[y] += 1
    elif infecting_cnt[x]<k and sick[x]==1:
        sick[x],sick[y] = 1,1
        infecting_cnt[x] += 1
    elif infecting_cnt[y]<k and sick[y]==1:
        sick[x],sick[y] = 1,1
        infecting_cnt[y] += 1

print(''.join(map(str, sick[1:])))