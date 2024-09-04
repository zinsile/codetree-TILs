n = int(input())
arr = input().split()
max1 = int(arr[0])
max2 = int(arr[1])

for elem in arr:
    elem = int(elem)
    if elem > max1:
        max1 = elem
    elif elem > max2:
        max2 = elem

print(max1, max2, end = ' ')