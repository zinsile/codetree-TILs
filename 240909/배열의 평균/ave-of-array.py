arr = [list(map(int, input().split())) for _ in range(2)]

for a in arr:
    avg = sum(a)/4
    print(f"{avg:.1f}", end=' ')
print()

for i in range(4):
    avg = (arr[0][i]+arr[1][i])/2
    print(f"{avg:.1f}", end=' ')
print()

temp = 0
for a in arr:
    temp += sum(a)
avg = temp/8
print(f"{avg:.1f}")