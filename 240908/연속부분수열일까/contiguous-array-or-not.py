n1,n2 = map(int, input().split())
aline = list(map(int, input().split()))
bline = list(map(int, input().split()))

cnt = 0
for i,a in enumerate(aline):
    if a in bline:
        cnt+=1
    elif a not in bline and cnt>0:
        print("No")
        cnt = 0

if cnt == len(bline):
    print("Yes")