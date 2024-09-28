n,c,g,h = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

max_n = 0
for i in range(1,22):
    num = 0
    for ta,tb in arr:
        if i < ta:
            num += c
        if ta<=i<=tb:
            num += g
        if i>tb:
            num += h
    max_n = max(max_n, num)
print(max_n)