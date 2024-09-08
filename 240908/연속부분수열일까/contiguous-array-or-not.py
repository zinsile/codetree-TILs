n1, n2 = map(int, input().split())
aline = list(map(int, input().split()))
bline = list(map(int, input().split()))
t = 0
for i in range(abs(n1 - n2) + 1):
    cnt = 0
    temp = []
    for a in aline[i:i + n2]:
        if a in bline:
            cnt += 1
            temp.append(a)
    if cnt == n2 and temp == bline:
        print("Yes")
        t = 1
        break

if t == 0:
    print("No")