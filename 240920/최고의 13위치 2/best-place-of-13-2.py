n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

def in_range(x,y):
    return x>=0 and x<n and y>=0 and y<n

curmax = 0

for i in range(n):
    for j in range(n-2):
        for k in range(i,n):
            for l in range(n-2):
                if i==k and j<=l<j+3:
                    l = l+(j+3-l)
                if not in_range(l+1,l+2):
                    continue
                if i==k and l+2>=k:
                    continue
                curmax = max(curmax, arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[k][l]+arr[k][l+1]+arr[k][l+2])

print(curmax)