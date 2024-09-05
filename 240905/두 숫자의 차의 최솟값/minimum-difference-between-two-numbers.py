n = int(input())
arr = list(map(int, input().split()))
mins = 100

for i in range(n-1):
    a,b = arr[i], arr[i+1]
    if mins > abs(a-b):
        mins = abs(a-b)

print(mins)