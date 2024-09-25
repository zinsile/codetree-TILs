MAX_NUM = 1000000
arr = list(map(int, input().split()))

min_p = MAX_NUM * 2
maxt, mint = 0, MAX_NUM * 2
for i in range(6):
    for j in range(6):
        if i==j:
            continue
        for k in range(6):
            if i==k or j==k:
                continue
            for l in range(6):
                if i==l or j==l or k==l:
                    continue
                t1 = arr[i]+arr[j]
                t2 = arr[k]+arr[l]
                t3 = sum(arr) - t1 - t2
                maxt = max(t1, t2, t3)
                mint = min(t1, t2, t3)
                min_p = min(min_p, maxt-mint)

print(min_p)