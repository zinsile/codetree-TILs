n1,n2 = map(int, input().split())
aline = list(map(int, input().split()))
bline = list(map(int, input().split()))

cnt = 0
for i,a in enumerate(aline):
    if a in bline and cnt==n2:
        continue
    elif cnt==n2:
        break
    elif a in bline:
        cnt+=1
    else:
        if 0<cnt:
            cnt = 0


if cnt == len(bline):
    print("Yes")
else:print("No")