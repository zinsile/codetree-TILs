n,m = map(int,input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
b.sort()

cnt = 0
for i in range(n-m+1):
    sub_a = a[i:i+m]
    sub_a.sort()
    if sub_a == b:
        cnt += 1
print(cnt)