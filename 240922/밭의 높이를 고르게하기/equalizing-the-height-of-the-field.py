import sys

n,h,t= map(int, input().split())
arr = list(map(int, input().split()))

min_power = sys.maxsize 
for i in range(n-t+1):
    power = 0
    for j in range(i,i+t):
        power += abs(h-arr[j])
    min_power = min(min_power,power)
print(min_power)