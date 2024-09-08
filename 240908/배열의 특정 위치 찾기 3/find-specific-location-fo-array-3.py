arr = list(map(int, input().split()))
for i,elem in enumerate(arr):
    if elem==0:
        index = i
        break
print(sum(arr[index-3:index]))