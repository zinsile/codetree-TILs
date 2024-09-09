n,k,p,t = map(int, input().split())
sick = [0]*(n+1)    #감염여부 : 정상-0, 감염-1
hand_shake = [list(map(int, input().split())) for _ in range(t)]
hand_shake.sort()
sick[p] = 1

for t,x,y in hand_shake:
    if k==0:
        break
    elif sick[x]==1 or sick[y]==1:
        sick[x],sick[y] = 1,1
        k -= 1

for i in sick[1:]:
    print(i,end='')