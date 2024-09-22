n = int(input())
arr = list(map(int, input().split()))

cnt = 0
for i in range(n):
    for j in range(i,n):
        val_ave = sum(arr[i:j+1])/abs((j+1)-i)
        if val_ave in arr[i:j+1]:
                cnt+=1
print(cnt)