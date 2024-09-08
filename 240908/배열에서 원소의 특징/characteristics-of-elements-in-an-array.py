arr = list(map(int, input().split()))
for i,elem in enumerate(arr):
    if elem%3==0:
        index = i
        break
print(arr[index-1])