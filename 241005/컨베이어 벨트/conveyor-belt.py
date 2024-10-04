n,t = map(int, input().split())
arr = [i for _ in range(2) for i in list(map(int, input().split()))]

for _ in range(t):
    temp = arr[2*n-1]
    for i in range(2*n-1,0,-1):
        arr[i] = arr[i-1]
    arr[0] = temp

for idx,a in enumerate(arr):
    if idx == n:
        print()
    print(a,end=' ')