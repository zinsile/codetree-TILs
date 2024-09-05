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
        continue
    elif elem in exs:
        elem.remove(elem)
        continue
    elif elem not in exs:
        exs.append(elem)
if maxs == -1 and len(exs)>0:
    for elem in exs:
        if elem > maxs:
            maxs = elem
print(maxs)