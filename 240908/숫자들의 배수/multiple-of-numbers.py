n = int(input())
arr = [n*(i+1) for i in range(10)]
cnt = 0
for i in arr:
    if i%5==0:
        cnt+=1
    print(i,end=' ')
    if cnt == 2:
        break