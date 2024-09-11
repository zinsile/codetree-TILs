n,m = map(int, input().split())
arr = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    r,c = map(int, input().split())
    arr[r][c] = 1

for raw in arr[1:]:
    for elem in raw[1:]:
        print(elem, end=' ')
    print()