n1,n2 = map(int, input().split())
aline = list(map(int, input().split()))
bline = list(map(int, input().split()))

cnt = 0
for i,a in enumerate(aline):
    if a in bline:
        cnt+=1
    else:
        if 0<cnt<n2:
            cnt = 0
        elif cnt == n2:
            continue

if cnt == len(bline):
    print("Yes")
else:print("No")

62 10
42 84 87 3 88 12 50 62 45 100 8 98 85 20 1 21 18 66 67 59 47 17 34 77 38 66 87 95 59 59 43 23 64 86 77 37 14 2 96 85 3 27 40 49 16 28 42 98 43 39 63 39 62 33 17 57 47 2 59 54 28 23 
23 64 86 77 37 14 2 96 85 3