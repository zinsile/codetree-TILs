MAX_NUM = 1000

arr = list(map(int, input().split()))

min_power = MAX_NUM*2

for i in range(5):
    for j in range(5):
        if i==j: continue
        for k in range(5):
            if i==k or j==k : continue
            t1 = arr[i] + arr[j]
            t2 = arr[k]
            t3 = sum(arr)-t1-t2
            if t1==t2 or t2==t3 or t1==t3:
                continue
            maxt = max(t1,t2,t3)
            mint = min(t1,t2,t3)
            min_power = min(min_power, maxt-mint)
print(min_power)