t, a, b = map(int, input().split())
arr = [list(map(str, input().split())) for _ in range(t)]

cnt = 0
for i in range(a,b+1):
    diff_s = 1000
    diff_n = 1000
    for a,x in arr:
        if a=='S':
            diff_s = min(diff_s, abs(int(x)-i))
        if a=='N':
            diff_n = min(diff_n, abs(int(x)-i))
    if diff_n >= diff_s:
        cnt += 1
print(cnt)