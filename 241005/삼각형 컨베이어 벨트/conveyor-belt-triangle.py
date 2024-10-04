n,t = map(int, input().split())
arr = [i for _ in range(3) for i in list(map(int, input().split()))]

for _ in range(t):
    temp = arr[3*n-1]
    for i in range(3*n-1,0,-1):
        arr[i] = arr[i-1]
    arr[0] = temp

for idx,elem in enumerate(arr):
    if idx % n == 0 and idx != 0:
        print()
    print(elem, end=' ')