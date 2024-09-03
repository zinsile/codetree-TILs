arr = input().split()

max_vlaue = 0
for elem in arr:
    elem = int(elem)
    if elem > max_vlaue:
        max_vlaue = elem

print(max_vlaue)