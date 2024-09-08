arr = list(map(int, input().split()))
even = []
for i in arr:
    if i == 0:
        break
    elif i%2==0:
        even.append(i)
print(len(even),sum(even),end=' ')