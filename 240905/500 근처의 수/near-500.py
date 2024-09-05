arr = list(map(int, input().split()))
maxs = 0
mins = 1001

for elem in arr:
    if elem < 500 and maxs < elem:
        maxs = elem
    elif elem >= 500 and mins > elem:
        mins = elem

print(maxs, mins, end = ' ')