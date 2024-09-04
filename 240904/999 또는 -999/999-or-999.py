import sys

arr = input().split()
mins = int(arr[0])
maxs = int(arr[0])

for elem in arr[1:]:
    elem = int(elem)
    if elem == -999 or elem==999:
        break
    elif elem < mins:
        mins = elem
    elif elem > maxs:
        maxs = elem

print(maxs,mins, end=' ')