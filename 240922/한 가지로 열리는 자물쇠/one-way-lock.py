n = int(input())
arr = list(map(int, input().split()))

cnt = 0
for i in range(1,n+1):
    for j in range(1,n+1):
        for k in range(1,n+1):
            temp = False
            temp_ls = [i,j,k]
            for l in range(3):
                if abs(temp_ls[l]-arr[l])<=2:
                    temp = True
            if temp: cnt+=1

print(cnt)