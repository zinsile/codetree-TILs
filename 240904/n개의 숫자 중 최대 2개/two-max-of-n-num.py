import sys
n = int(input())
arr = input().split()
max1 = -sys.maxsize
max2 = -sys.maxsize

for elem in arr:
    elem = int(elem)
    if elem > max1:
        max1 = elem
    elif elem > max2:
        max2 = elem

print(max1, max2, end = ' ')