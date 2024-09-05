n = int(input())
arr = list(map(int, input().split()))
maxs = -1
gap = 0

for i in range(n):
    elem = arr[i]
    for elem2 in arr[i+1:]:
        gap = elem2 - elem
        if gap > maxs:
            maxs = gap

print(maxs)