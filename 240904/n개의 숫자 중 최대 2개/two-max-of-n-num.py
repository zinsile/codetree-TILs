n = int(input())
arr = input().split()
max1 = arr[0]
max2 = arr[0]

for elem in arr[1:]:
    elem = int(elem)
    if elem > max1:
        max1 = elem
    elif elem > max2:
        max2 = elem

print(max1, max2, end = ' ')