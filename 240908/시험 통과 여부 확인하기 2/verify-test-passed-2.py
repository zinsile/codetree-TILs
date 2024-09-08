n = int(input())
cnt = 0
for i in range(n):
    score = list(map(int, input().split()))
    avg = sum(score)/4
    if avg >= 60:
        print("pass")
        cnt += 1
    else: print("fail")
print(cnt)