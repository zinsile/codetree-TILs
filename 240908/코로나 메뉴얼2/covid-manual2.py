h = [0]*4
for _ in range(3):
    a,b = tuple(map(str, input().split()))
    b = int(b)
    if a == 'Y' and b>=37:
        h[0] += 1
    elif a == 'N' and b>=37:
        h[1]+=1
    elif a=='Y' and b<37:
        h[2]+=1
    elif a=='N' and b<37:
        h[3]+=1
for i in h:
    print(i,end=' ')
if h[0]>=2:
    print('E')