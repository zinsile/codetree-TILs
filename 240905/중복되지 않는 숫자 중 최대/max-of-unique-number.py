n = int(input())
arr = input().split()
exs = []
maxs = -1
for elem in arr[1:]:
    elem = int(elem)
    if elem == maxs:
        maxs = -1
        continue
    elif elem > maxs:
        maxs = elem

print(maxs)