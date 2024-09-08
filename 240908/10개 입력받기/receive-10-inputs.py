arr = list(map(int, input().split()))
index = len(arr)
for i,elem in enumerate(arr):
    if elem==0:
        index = i
        break
arrsum = sum(arr[:index])
arravg = arrsum/index
print(f"{arrsum} {arravg:.1f}")