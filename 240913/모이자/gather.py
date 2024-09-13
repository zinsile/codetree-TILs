import sys
INT_MIN = sys.maxsize
n = int(input())
fams = list(map(int, input().split()))

for i in range(n):
    dis = 0
    for j in range(i):
        dis += fams[j]*(i-j)
    for k in range(n-i):
        dis += fams[i+k]*k
    INT_MIN = min(dis,INT_MIN)

print(INT_MIN)