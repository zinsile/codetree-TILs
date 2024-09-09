arr = [list(map(int, input().split())) for _ in range(4)]
result = 0
for i in range(4):
    if i==3:
        result += sum(arr[i])
    else:
        result += sum(arr[i][:i+1])
print(result)